import frappe
from frappe.model.document import Document

class NameCard(Document):
	def validate(self):
		# Concatenate first_name and last_name to set full_name
		self.full_name = (self.first_name or "") + " " + (self.last_name or "")
