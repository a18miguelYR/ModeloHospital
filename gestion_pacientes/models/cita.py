from odoo import api, fields, models

class Cita(models.Model):
    _name="hospital.appointment"
    _inherit=['mail.thread','mail.activity.mixin']
    _description="Cita en el hospital"

    patient_id= fields.Many2one('hospital.patient', string="Patient")
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender", related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment Time')
    booking_date = fields.Date(string='Booking Date')
    

