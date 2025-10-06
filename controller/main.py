from odoo import http
from odoo.http import request

class PmantNotify(http.Controller):

    @http.route('/pmant/notify/poll', type='json', auth='user')
    def poll(self):
        user = request.env.user
        notifs = request.env['pmant.notification'].sudo().search([
            ('user_id', '=', user.id),
        ])
        return [
            {
                'id': n.id,
                'title': n.title,
                'message': n.message,
                'type': n.type,
                'sticky': n.sticky,
            }
            for n in notifs
        ]

    @http.route('/pmant/notify/ack', type='json', auth='user')
    def ack(self, ids):
        request.env['pmant.notification'].sudo().browse(ids).unlink()
        return True
