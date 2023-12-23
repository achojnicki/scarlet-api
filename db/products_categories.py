class products_categories:
	def get_products_categories(self, limit, skip):
		products_categories=[]
		cursor=self.products_categories.find().skip(skip).limit(limit)
		
		for item in cursor:
			products_categories.append(item)
			
		return products_categories

	def get_products_category_by_products_category_seo_name(self, products_category_seo_name):
		query={'products_category_seo_name': products_category_seo_name}

		products_category=self.products_categories.find_one(query)
		return products_category
		