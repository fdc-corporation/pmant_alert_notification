from odoo import fields, http
from odoo.http import request

class PmantNotify(http.Controller):

    @http.route('/pmant/notify/poll', type='jsonrpc', auth='user')
    def poll(self):
        user = request.env.user
        notifs = request.env['pmant.notification'].sudo().search([
            ('user_id', '=', user.id),
            ('scheduled_at', '<=', fields.Datetime.now()),
        ], order='scheduled_at, id', limit=20)
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

    @http.route('/pmant/notify/ack', type='jsonrpc', auth='user')
    def ack(self, ids):
        request.env['pmant.notification'].sudo().search([
            ('id', 'in', ids),
            ('user_id', '=', request.env.user.id),
        ]).unlink()
        return True
