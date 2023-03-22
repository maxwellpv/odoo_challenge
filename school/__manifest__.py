{
    'name': 'School',
    'version': '1.0',
    'summary': 'My first module',
    'sequence': 5,
    'description': "",
    'author': "Maxwell",
    'category': 'Custom',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/subject.xml',
        'views/student.xml',
        'views/teacher.xml',
    ],
    'application': True,
}
