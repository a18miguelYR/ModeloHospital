from datetime import date
from odoo import api, fields, models

class CentroSaludPaciente(models.Model):
    _name="hospital.patient"
    _inherit=['mail.thread','mail.activity.mixin']
    _description="centro de salud"

    name=fields.Char(string="Name",)
    dni=fields.Char(string="Dni",)
    date_of_birth= fields.Date(string="Date of birth")
    ref=fields.Char(string="Reference", tracking=True)
    age=fields.Integer(string="Age", compute='_compute_age', tracking=True)
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender", tracking=True)
    active = fields.Boolean(string="Active", default=True)

    #Conseguir la edad con la fecha
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age=  today.year - rec.date_of_birth.year
            else:
                rec.age=1
    
