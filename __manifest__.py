{
    'name': 'Alertas por fechas CRM y Mantenimiento',
    'version': '1.0',
    'description': 'Módulo para gestionar alertas por fechas en CRM y Mantenimiento',
    'author': 'Yostin Palacios',
    'website': 'https://equiposindustriales.pe/',  # Cambia a tu sitio web si aplica
    'license': 'LGPL-3',
    'category': 'Sales',
    'depends': [
        'base',
        'web',
        'pmant',
        'maintenance',
        'oc_compras',
        "mail",
        "crm",
        "sale",
        "account",
    ],
    'data': [
        "security/ir.model.access.csv",
        # ACCIONES DE SERVIDOR
        "view/server/action_alarm.xml",
        # PLANTILLAS DE MODELOS
        "view/from_mant_inherit.xml",
        "view/from_etapa_mant_inherit.xml",
        "view/form_crm_inherit.xml",
        "view/form_sale_inherit.xml",
        # "view/from_account_inherit.xml",
        #PLANTILLAS DE EMAIL 
        "view/email/email_notification.xml",
        "view/email/email_notification_crm.xml",
    ],
    'assets': {
        "web.assets_backend": [
            "pmant_alert_notification/static/src/js/pmant_notifier.js",
        ]
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
