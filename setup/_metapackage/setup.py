import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-oca-purchase-workflow",
    description="Meta package for oca-purchase-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-product_by_supplier',
        'odoo11-addon-product_supplierinfo_discount',
        'odoo11-addon-purchase_discount',
        'odoo11-addon-purchase_exception',
        'odoo11-addon-purchase_landed_cost',
        'odoo11-addon-purchase_line_procurement_group',
        'odoo11-addon-purchase_minimum_amount',
        'odoo11-addon-purchase_order_approval_block',
        'odoo11-addon-purchase_order_approved',
        'odoo11-addon-purchase_order_line_stock_available',
        'odoo11-addon-stock_landed_cost_company_percentage',
        'odoo11-addon-subcontracted_service',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
