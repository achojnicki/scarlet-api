class Products:
    def __init__(self, root):
        self._root=root

        self.config=self._root.config
        self.log=self._root.log
        self.db=self._root.db

    def get_products(self, page):
        limit=self.config.api.results_per_page
        skip=(int(page)-1)*limit

        products={}
        data=self.db.get_products(
            limit=limit,
            skip=skip,
            )
        
        for item in data:
            del item['_id']

        for product in data:
            products[product['product_seo_name']]=product
        
        self.log.success('Obtained products')

        return products

    def get_product(self, product_seo_name:str):
        product=self.db.get_product_by_product_seo_name(
            product_seo_name=product_seo_name
            )

        del product['_id']
        self.log.success('Obtained details about a short URL')
        return product

    def get_products_by_product_tag(self, page, tag):
        limit=self.config.api.results_per_page
        skip=(int(page)-1)*limit

        products={}
        data=self.db.get_products_by_product_tag(
            limit=limit,
            skip=skip,
            tag=tag)

        for item in data:
            del item['_id']

        for product in data:
            products[product['product_seo_name']]=product
        
        self.log.success('Obtained products by tag')

        return products