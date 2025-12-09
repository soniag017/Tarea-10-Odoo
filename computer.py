from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date
 
class PCComputer(models.Model):
    _name = 'pc.computer'
    _description = 'Ordenador de la empresa'
 
    number = fields.Char("Número de equipo", required=True)
    user_id = fields.Many2one("res.users", string="Usuario")
    components_ids = fields.Many2many("pc.component", string="Componentes")
    last_mod = fields.Date("Última modificación")
    total_price = fields.Monetary("Precio total", compute="_compute_total", store=True)
    issues = fields.Text("Incidencias")
 
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id)
 
    # Restricción: fecha futura prohibida
    @api.constrains('last_mod')
    def _check_last_mod(self):
        for record in self:
            if record.last_mod and record.last_mod > date.today():
                raise ValidationError("La fecha no puede ser futura")
 
    # Cálculo automático del precio total
    @api.depends("components_ids.price")
    def _compute_total(self):
        for record in self:
            record.total_price = sum(record.components_ids.mapped("price"))
