from odoo import models, fields
 
class PCComponent(models.Model):
    _name = 'pc.component'
    _description = 'Componente del PC'
 
    name = fields.Char("Nombre técnico", required=True)
    specs = fields.Text("Especificaciones")
    price = fields.Monetary("Precio")
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id)
