# -*- coding: utf-8 -*-
from odoo import http


class InvoicePaymentReport(http.Controller):
    @http.route('/invoice_payment_report/invoice_payment_report', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/invoice_payment_report/invoice_payment_report/objects', auth='public')
    def list(self, **kw):
        return http.request.render('invoice_payment_report.listing', {
            'root': '/invoice_payment_report/invoice_payment_report',
            'objects': http.request.env['invoice_payment_report.invoice_payment_report'].search([]),
        })

    @http.route('/invoice_payment_report/invoice_payment_report/objects/<model("invoice_payment_report.invoice_payment_report"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('invoice_payment_report.object', {
            'object': obj
        })
