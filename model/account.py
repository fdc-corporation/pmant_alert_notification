from odoo import models, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = "account.move"

    def action_post(self):
        # Primero ejecuta el posteo normal (aquí se asigna correlativo)
        res = super().action_post()

        # Luego validamos con UserError
        for record in self:
            if record.estado_sunat not in ["01", "05"]:
                raise UserError(_(f"La factura {record.name} no fue aceptada por la SUNAT / {record.p_response}"))

        return res
