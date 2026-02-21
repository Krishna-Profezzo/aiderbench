import frappe
import re

def validate(self):
    # Validate PAN number format
    if self.pan_number:
        if not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', self.pan_number):
            frappe.throw("Invalid PAN Number format")
    
    # Validate mobile number is exactly 10 digits
    if self.mobile_number:
        if not re.match(r'^\d{10}$', str(self.mobile_number)):
            frappe.throw("Invalid Mobile Number")
