from flask_restful import fields, marshal_with

from dao.product_dao import ProductDao
from models.product_model import ProductModel
from resources.base_resource import BaseResource


class ProductResource(BaseResource):
    fields = {
        "id_": fields.Integer,
        "sku": fields.String,
        "name": fields.String,
        "description": fields.String,
        "price": fields.Float,
        "height": fields.Float,
        "width": fields.Float,
        "length": fields.Float,
        "weight": fields.Float
    }

    def __init__(self):
        self.__dao = ProductDao()
        self.__model_type = ProductModel
        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def get(self, id=None):
        return super().get(id)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self, id):
        return super().put(id)

    @marshal_with(fields)
    def delete(self, id):
        return super().delete(id)
