import frappe
import re

def validate(self):
    # Validate pin is exactly 6 digits
    if self.pin:
        if not re.match(r'^\d{6}$', str(self.pin)):
            frappe.throw("Pin must be 6 digits")
