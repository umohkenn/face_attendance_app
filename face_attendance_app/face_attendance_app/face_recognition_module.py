"""Utility functions for face recognition."""

import os
import pickle
from typing import Optional

import face_recognition
import frappe

# Directory to store face encodings
DATA_PATH = frappe.get_site_path('private', 'employee_faces')
ENCODINGS_FILE = os.path.join(DATA_PATH, 'encodings.pkl')


def train():
    """Generate face encodings from Employee Face doctypes."""
    os.makedirs(DATA_PATH, exist_ok=True)
    encodings = {}
    for doc in frappe.get_all('Employee Face', fields=['name', 'image']):
        if not doc.image:
            continue
        file_path = frappe.get_site_path(doc.image)
        img = face_recognition.load_image_file(file_path)
        face_enc = face_recognition.face_encodings(img)
        if face_enc:
            encodings[doc.name] = face_enc[0]
    with open(ENCODINGS_FILE, 'wb') as f:
        pickle.dump(encodings, f)
    return len(encodings)


def identify_employee(image_bytes: bytes) -> Optional[frappe.model.document.Document]:
    """Return Employee doc if a matching face is found."""
    if not os.path.exists(ENCODINGS_FILE):
        return None
    with open(ENCODINGS_FILE, 'rb') as f:
        encodings = pickle.load(f)
    unknown_img = face_recognition.load_image_file(image_bytes)
    unknown_encodings = face_recognition.face_encodings(unknown_img)
    if not unknown_encodings:
        return None
    unknown_enc = unknown_encodings[0]
    for employee_name, face_enc in encodings.items():
        match = face_recognition.compare_faces([face_enc], unknown_enc, tolerance=0.6)
        if match[0]:
            return frappe.get_doc('Employee', employee_name)
    return None
