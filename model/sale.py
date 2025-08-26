from odoo import models, fields, api, _
from odoo.exceptions import UserError



class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Ventas"

    is_servicio = fields.Boolean(string="Es servicio", compute="verify_service")

    def action_open_wizard_sale(self):
        return {
            "name": "Confirmacion de venta",
            "type": "ir.actions.act_window",
            "res_model": "wizard.sale.order",
            "view_mode": "form",
            "target": "new",
            "context": {"default_order_id": self.id},
        }  


    def verify_service(self):
        for order in self:
            order.is_servicio = any(
                line.product_template_id.detailed_type == "service"
                for line in order.order_line
            )


class WizardConfirmSaleOrder(models.TransientModel):
    _name = "wizard.sale.order"
    _description = "Wizard Sale Order"

    sale_id = fields.Many2one("sale.order", string="Venta", default= lambda self: self.env.context.get("default_order_id"))


    def confirm_sale(self):
        self.sale_id.action_confirm()