from odoo import http, fields
from odoo.http import request

class PmantNotify(http.Controller):
    @http.route('/pmant/notify/poll', type='json', auth='user')
    def poll(self):
        uid = request.env.user.id
        now = fields.Datetime.now()
        recs = request.env['pmant.notification'].sudo().search([
            ('user_id', '=', uid),
            ('is_sent', '=', False),
            ('scheduled_at', '<=', now),
        ], limit=20)
        return [
            {
                'id': n.id,
                'title': n.title,
                'message': n.message,
                'type': n.type or 'info',
                'sticky': bool(n.sticky),
            } for n in recs
        ]

    @http.route('/pmant/notify/ack', type='json', auth='user')
    def ack(self, ids):
        request.env['pmant.notification'].sudo().browse(ids).write({
            'is_sent': True,
            'sent_at': fields.Datetime.now(),
        })
        return True
