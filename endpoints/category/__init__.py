from response import Response

class category:
    def category(self, products_category_seo_name:str, **kwargs):
        rsp=Response()

        try:
            products_category=self._middlewares.products_categories.get_products_category(
                products_category_seo_name=products_category_seo_name
                )
            rsp.status="Success"
            rsp.message="Products Category"
            rsp.data[products_category_seo_name]=products_category

        except:
            rsp.status="Error"
            rsp.message="Unable to find products category"
        return rsp