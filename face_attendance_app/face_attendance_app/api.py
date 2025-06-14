import base64
from io import BytesIO

import frappe
from frappe import _
from .face_recognition_module import identify_employee
from .mask_detection_module import detect_mask
from .liveness_detection_module import detect_blink

@frappe.whitelist(allow_guest=True)
def mark_attendance(image: str) -> dict:
    """Identify employee from image data URL and create Attendance."""
    header, data = image.split(',')
    image_bytes = BytesIO(base64.b64decode(data))

    # Basic liveness and mask checks
    if not detect_blink(None):
        frappe.throw(_('Liveness check failed'))
    if not detect_mask(image_bytes):
        frappe.throw(_('Please wear a mask'))

    employee = identify_employee(image_bytes)
    if not employee:
        return {'status': 'fail'}

    attendance = frappe.get_doc({
        'doctype': 'Attendance',
        'employee': employee.name,
        'status': 'Present',
        'attendance_date': frappe.utils.today(),
    })
    attendance.insert(ignore_permissions=True)
    frappe.db.commit()
    return {'status': 'success', 'employee': employee.employee_name}
