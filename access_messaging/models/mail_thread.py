from openerp.osv import fields, osv, orm
from lxml import etree
try:
    import simplejson as json
except ImportError:
    import json
from openerp.addons.mail.mail_thread import mail_thread


def fields_view_get(self, cr, uid, view_id=None, view_type='form', context=None, toolbar=False, submenu=False):
    res = super(mail_thread, self).fields_view_get(cr, uid, view_id=view_id, view_type=view_type, context=context, toolbar=toolbar, submenu=submenu)
    if view_type == 'form':
        doc = etree.XML(res['arch'])
        for node in doc.xpath("//field[@name='message_ids']"):
            options = json.loads(node.get('options', '{}'))
            options.update(self._get_user_chatter_options(cr, uid, context=context))
            node.set('options', json.dumps(options))
        for node in doc.xpath("//div[hasclass('oe_chatter')]"):
            if not self.pool['res.users'].has_group(cr, uid, 'access_messaging.group_messaging'):
                node.getparent().remove(node)
        res['arch'] = etree.tostring(doc)
    return res

mail_thread.fields_view_get = fields_view_get
