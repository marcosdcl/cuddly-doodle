from models.base_model import BaseModel
from sqlalchemy import Column, String, Float
from sqlalchemy.orm import validates
from utils.validators import (
    validate_type, validate_max_length, validate_not_empty, 
    validate_number_greater_than_zero, validate_characteres_equal_to
)


class ProductModel(BaseModel):
    __tablename__= 'products'

    sku = Column('sku', String(length=13), nullable=False)
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=250), nullable=False)
    price = Column('price', Float, nullable=False)
    height = Column('height', Float, nullable=False)
    width = Column('width', Float, nullable=False)
    length = Column('length', Float, nullable=False)
    weight = Column('weight', Float, nullable=False)

    def __init__(self, sku: str, name: str, description: str, 
                price: float, height: float, width: float, 
                length: float, weight: float) -> None:
        self.sku = sku
        self.name = name
        self.description = description
        self.price = price
        self.height = height
        self.width = width
        self.length = length
        self.weight = weight

    @validates('sku')
    def validate_sku(self, key, sku):
        sku = validate_type(key, sku, str)
        return validate_characteres_equal_to(key, sku, 13)

    @validates('name')
    def validate_name(self, key, name):
        name = validate_type(key, name, str)
        name = validate_not_empty(key, name)
        return validate_max_length(key, name, 100)

    @validates('description')
    def validate_description(self, key, description):
        description = validate_type(key, description, str)
        description = validate_not_empty(key, description)
        return validate_max_length(key, description, 250)

    @validates('price')
    def validate_price(self, key, price):
        price = validate_type(key, price, float)
        return validate_number_greater_than_zero(key, price)

    @validates('height')
    def validate_height(self, key, height):
        height = validate_type(key, height, float)
        return validate_number_greater_than_zero(key, height)

    @validates('width')
    def validate_width(self, key, width):
        width = validate_type(key, width, float)
        return validate_number_greater_than_zero(key, width)

    @validates('length')
    def validate_length(self, key, length):
        length = validate_type(key, length, float)
        return validate_number_greater_than_zero(key, length)

    @validates('weight')
    def validate_weight(self, key, weight):
        weight = validate_type(key, weight, float)
        return validate_number_greater_than_zero(key, weight)
