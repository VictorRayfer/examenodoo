# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import timedelta,date,datetime
from dateutil.relativedelta import relativedelta

class animal(models.Model):
    _name = 'zoo.animal'
    _inherit = 'base.entidad'
    nombre = fields.Char()
    fechanacimiento = fields.Date()
    idszoologicos=fields.Many2many(string= "zoologicos",comodel_name='zoo.zoologico',relation = 'rel_zoologicos_animales',column1='zoologico', column2='animal')

class zoologico(models.Model):
    _inherit = 'base.empresa'
    nombre = fields.Char()
    maxanimales = fields.Integer()
    idsanimales=fields.Many2many(string= "animales",comodel_name='zoo.animal',relation = 'rel_zoologicos_animales',column1='animal', column2='zoologico')
    idshabitats=fields.Many2many(string="habitats",comodel_name='zoo.habitat',relation = 'rel_zoologicos_habitats',column1='habitat', column2='zoologico')

class habitat(models.Model):
    _name = 'zoo.habitat'
    nombre = fields.Char()
    tipo = fields.Selection(
        selection=[('jl', 'jaula'), ('ab', 'abierto'), ('iv', 'invernadero')])
    idszoologicos=fields.Many2many(string="zoologicos",comodel_name='zoo.zoologico',relation = 'rel_zoologicos_habitats',column1='zoologico', column2='habitat')

class tratamiento(models.Model):
    _name = 'zoo.tratamiento'
    nombre = fields.Char()
    horas = fields.Integer()
