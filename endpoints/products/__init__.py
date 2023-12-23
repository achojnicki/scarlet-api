from response import Response

class products:
    def products(self, page=1, **kwargs):
        rsp=Response()

        products=self._middlewares.products.get_products(
            page=page
            )
        
        rsp.status="Success"
        rsp.message="Products"
        rsp.data=products
        
        return rsp