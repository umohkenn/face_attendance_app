from setuptools import setup, find_packages

setup(
    name='face_attendance_app',
    version='0.1.0',
    description='Face ID attendance app for Frappe/ERPNext with mask and liveness detection',
    author='umohkenn',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'frappe>=13.0.0',
        'face_recognition',
        'opencv-python',
        'tensorflow>=2.0.0',
        'numpy',
        'Pillow'
    ],
)
