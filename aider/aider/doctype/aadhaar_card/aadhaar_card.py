import frappe
import re

def validate(self):
    # Validate Aadhaar number is exactly 12 digits
    if self.aadhaar_number:
        if not re.match(r'^\d{12}$', str(self.aadhaar_number)):
            frappe.throw("Invalid Aadhaar Number")
    
    # Validate mobile number is exactly 10 digits
    if self.mobile_number:
        if not re.match(r'^\d{10}$', str(self.mobile_number)):
            frappe.throw("Invalid Mobile Number")
