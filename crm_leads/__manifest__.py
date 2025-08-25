# -*- coding: utf-8 -*-
{
    "name": "CRM: Order Lines on Opportunity (linked to Sales)",
    "summary": "Add Order Lines tab in CRM and copy them to Quotation on New Quotation.",
    "version": "1.0.0",
    "license": "LGPL-3",
    "depends": ["crm", "sale_management"],  # ensure Sales/Quotations
    "data": [
        "security/ir.model.access.csv",
        "views/crm_orderlines.xml",
    ],
    "application": False,
    "installable": True,
}
