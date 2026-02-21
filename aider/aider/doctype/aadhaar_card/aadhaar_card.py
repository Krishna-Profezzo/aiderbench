import frappe
import re
from frappe.model.document import Document

class AadhaarCard(Document):
    def validate(self):
        if self.aadhaar_number:
            if not re.match(r'^\d{12}$', str(self.aadhaar_number)):
                frappe.throw("Aadhaar Number must be exactly 12 digits")
        if self.mobile_number:
            if not re.match(r'^\d{10}$', str(self.mobile_number)):
                frappe.throw("Mobile Number must be exactly 10 digits")
