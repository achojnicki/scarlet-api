from response import Response

class categories:
    def categories(self, page=1, **kwargs):
        rsp=Response()

        products=self._middlewares.products_categories.get_products_categories(
            page=page
            )
        
        rsp.status="Success"
        rsp.message="Products Categories"
        rsp.data=products
        
        return rsp