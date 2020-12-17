from odoo import api, fields, models
from odoo.addons.http_routing.models.ir_http import slug
from odoo.exceptions import UserError
class customers(models.Model):
    _name = 'carrent.customers'
    _description = 'carrent customers'
    id=fields.Integer("customer id",required=True)
    customer_name = fields.Char("customer Name", required=True, )
    address=fields.Char("address", required=True, )
    phone=fields.Integer("phone Number",required=True)
    email=fields.Char("email")
    def open_bookings_ofthe_customer(self):
      return {
      	'name':_('open_bookings_ofthe_customer'),
      	'domain':[('customers_id','=','self.id')],
      	'view_type':'form',
      	'res_model':'carrent.bookings',
      	'view_id': False,
      	'view_mode':'tree,form',
      	'type':'ir.actions.act_window',
      
      }
    
