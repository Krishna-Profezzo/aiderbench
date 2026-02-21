import frappe
import re
from frappe.model.document import Document

class AadhaarCard(Document):
    def validate(self):
        # Validate Aadhaar Number
        if self.aadhaar_number:
            if not re.match(r'^\d{12}$', str(self.aadhaar_number)):
                frappe.throw("Aadhaar Number must be exactly 12 digits")
        # Validate Mobile Number
        if self.mobile_number:
            if not re.match(r'^\d{10}$', str(self.mobile_number)):
                frappe.throw("Mobile Number must be exactly 10 digits")
        # City field is present but no validation is required
