from response import Response

class product:
    def product(self, product_seo_name:str, **kwargs):
        rsp=Response()

        try:
            product=self._middlewares.products.get_product(
                product_seo_name=product_seo_name
                )
            rsp.status="Success"
            rsp.message="Product"
            rsp.data[product_seo_name]=product

        except:
            rsp.status="Error"
            rsp.message="Unable to find product"
        return rsp