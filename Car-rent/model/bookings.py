from odoo import api, fields, models
from odoo.addons.http_routing.models.ir_http import slug
from odoo.exceptions import UserError

class bookings(models.Model):
    _name = 'carrent.bookings'
    _description = 'carrent bookings'
    booking_id=fields.Integer("booking id",required=True)
    car_number=fields.Integer("car Number",required=True)
    customer_id=fields.Integer("customer id",required=True)
    booking_from=fields.Date("booked from",required=True)
    booked_till=fields.Date("booked till",required=True)
    price=fields.Integer("price",required=True)
    state=fields.Selection([('draft','draft'),('confirm','confirmed') ,('cancel','canceled')],default='draft')
    last_modification=fields.Datetime(readonly="true")
    def write(self,values):
      values['last_modification']=fields.Datetime.now()
      return super(bookings,self).write(values)
    def unlink(self):
      for bookings in self:
         if bookings.state=='confirm':
            raise UserError("you can not delete confirmed orders")
      return super(bookings,self).unlink()
    
