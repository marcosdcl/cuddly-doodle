from models.product_model import ProductModel
from dao.base_dao import BaseDao


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__(ProductModel)
