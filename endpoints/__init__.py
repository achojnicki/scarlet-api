from endpoints import (
    login,
    logout,
    product,
    products,
    tag,
    category,
    categories
    )

class Endpoints(login.login,
    logout.logout,
    product.product,
    products.products,
    tag.tag,
    category.category,
    categories.categories,
    ):
    def __init__(self, root):
        self._root=root

        self._middlewares=root.middlewares
        self._log_handle=root.log_handle

        self._endpoints_with_required_login=[
            self.logout,
            ]