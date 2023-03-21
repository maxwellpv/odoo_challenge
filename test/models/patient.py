from odoo import api, fields, models


class SchoolSubject(models.Model):
    _name = "school.subject"
    name = fields.Char(string="Name", required=True)
    credits = fields.Integer(string="Credits", required=True)
    max_students = fields.Integer(string="Max Students", required=True)
    active = fields.Boolean(string="Active", required=True)
    # student_ids = fields.Many2many
    # teacher_id = fields.Many2one.id
