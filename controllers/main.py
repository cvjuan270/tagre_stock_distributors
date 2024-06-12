from odoo import http
from odoo.http import request 


class Main(http.Controller):
    @http.route(['/distributors/stock', '/distributors/stock/page/<int:page>'], type='http', auth='user', website=True)
    def products(self, page=1, search=None, **post):
        domain = [('detailed_type', '=', 'product')]
        if search:
            domain = domain + [('name', 'ilike', search)]
        post['search'] = search
        product_obj = http.request.env['product.product'].sudo().search(domain)
        search_count = product_obj.search_count(domain)
        page_detail = request.website.pager(
            url="/distributors/stock",
            total=search_count,
            page=page,
            step=12,
        )
        offset = page_detail['offset']
        product_obj = product_obj[offset: offset + 12]
        return request.render(
            'tagre_stock_distributors.stock_distributors',
            {
                'search': search,
                'products': product_obj,
                'pager': page_detail,
                'search_count': search_count,
            },
        )