from odoo import api, fields, models


class SchoolSubject(models.Model):
    _name = "school.subject"
    name = fields.Char(string="Name", required=True)
    credits = fields.Integer(string="Credits", required=True)
    max_students = fields.Integer(string="Max Students", required=True)
    active = fields.Boolean(string="Active", required=True)
    student_ids = fields.Many2many('school.student', string='Students')
    teacher_id = fields.Many2one('school.teacher', string='Teacher')


class SchoolStudent(models.Model):
    _name = "school.student"
    name = fields.Char(string="Name", required=True)
    birth_date = fields.Date(string="Birth Date", required=True)
    age = fields.Integer(string="Age", required=True)
    final_exam_grade = fields.Float(string="Final Exam Grade", required=True)
    subject_ids = fields.Many2many('school.subject', string='Subjects')


class SchoolTeacher(models.Model):
    _name = "school.teacher"
    name = fields.Char(string="Name", required=True)
    profile = fields.Text(string="Profile", required=True)
    subject_ids = fields.One2many('school.subject', 'teacher_id', string='Subjects')
