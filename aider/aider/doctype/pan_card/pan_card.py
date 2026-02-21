import frappe
import re
from frappe.model.document import Document

class PanCard(Document):
    def validate(self):
        if self.pan_number:
            if not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', str(self.pan_number)):
                frappe.throw("Invalid PAN Number format. Expected: ABCDE1234F")
        if self.mobile_number:
            if not re.match(r'^\d{10}$', str(self.mobile_number)):
                frappe.throw("Mobile Number must be exactly 10 digits")
