class products:
	def get_product_by_product_seo_name(self, product_seo_name):
		query={'product_seo_name': product_seo_name}

		product=self.products.find_one(query)
		return product

	def get_products(self, limit, skip):
		products=[]
		cursor=self.products.find().skip(skip).limit(limit)
		
		for item in cursor:
			products.append(item)
			
		return products

	def get_products_by_product_tag(self, limit, skip, tag):
		products=[]
		query={"product_tags": tag}
		cursor=self.products.find(query).skip(skip).limit(limit)

		for item in cursor:
			products.append(item)

		return products