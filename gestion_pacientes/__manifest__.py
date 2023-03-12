{
    'name': 'gestion de pacientes',
    'summary': 'Un modulo para la gestion de paceintes.',
    'description': """
        Sistema de gestion de pacientes para un centro de salud
    """,
    'author': 'a18miguelyr',
    'sequence':-100,
    'category': 'Salud',
    'version': '0.1',
    'depends': ['base','mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/male_patient_view.xml',
        'views/appointment_view.xml',
    ],
    'auto_install': False,
    'application': True,
}
