# Face Attendance App

This Frappe application allows employees to check in using facial recognition and automatically records attendance in ERPNext. Mask detection and basic liveness checks are included. The front end is inspired by the Zoho People check‑in kiosk, with a clean form and large check‑in button.

## Features
- Face recognition sign in
- Optional mask detection
- Basic liveness detection
- Face enrollment portal
- Kiosk web page for desktops and mobiles
- Automatic creation of ERPNext Attendance records

## Installation

Ensure you have a working Frappe bench or Frappe Cloud site.

```bash
bench get-app face_attendance_app <repository-url>
bench --site yoursite install-app face_attendance_app
bench build
bench restart
```

After installing, visit `/face_kiosk` to start the kiosk.

## Configuration

1. Upload employee images using the **Employee Face** doctype.
2. Train encodings by running `bench execute face_attendance_app.face_recognition_module.train`.
3. Place a camera in front of your kiosk and open the check‑in page.

## Development

To contribute, clone the repository, make changes, then push to GitHub.

```bash
git add .
git commit -m "Describe your changes"
git push origin main
```

