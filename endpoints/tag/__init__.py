from response import Response

class tag:
    def tag(self, tag, page=1, **kwargs):
        rsp=Response()

        products=self._middlewares.products.get_products_by_product_tag(
            tag=tag,
            page=page
            )
        
        rsp.status="Success"
        rsp.message="Products by tag"
        rsp.data=products
        
        return rsp