from odoo import fields, models

class MyFirstModel(models.Model):
    _name = "my.first.model"
    _description = "Nosso primeiro modelo criado no Odoo"

    my_first_field_integer = fields.Integer(string="Número Inteiro", required=True)

    