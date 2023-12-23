class Products_Categories:
    def __init__(self, root):
        self._root=root

        self.config=self._root.config
        self.log=self._root.log
        self.db=self._root.db

    def get_products_categories(self, page):
        limit=self.config.api.results_per_page
        skip=(int(page)-1)*limit

        products_categories={}
        data=self.db.get_products_categories(
            limit=limit,
            skip=skip,
            )
        
        for item in data:
            del item['_id']

        for products_category in data:
            products_categories[products_category['products_category_seo_name']]=products_category
        
        self.log.success('Obtained products categories')

        return products_categories

    def get_products_category(self, products_category_seo_name:str):
        products_category=self.db.get_products_category_by_products_category_seo_name(
            products_category_seo_name=products_category_seo_name
            )

        del products_category['_id']
        self.log.success('Obtained details about product category')
        return products_category