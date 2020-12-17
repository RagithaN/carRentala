from odoo import api, fields, models, _
from odoo.addons.http_routing.models.ir_http import slug
from odoo.exceptions import UserError

class cars(models.Model):
    _name ='carrent.cars'
    _description = 'carrent cars'
    id=fields.Integer("car Number",required=True)
    owner_name = fields.Char("car Name", required=True, )
    make=fields.Char("car Name", required=True, )
    year_of_manufactur=fields.Integer("car Number",required=True)
    bookings_count=fields.Integer(compute='_compute_bookings_count', store=True,string="total bookings")
    def open_bookings_ofthe_car(self):
      return {
      	'name':_('open_bookings_ofthe_car'),
      	'domain':[('cars_id','=','self.id')],
      	'view_type':'form',
      	'res_model':'carrent.bookings',
      	'view_id': False,
      	'view_mode':'tree,form',
      	'type':'ir.actions.act_window',
      
      }
    
     
