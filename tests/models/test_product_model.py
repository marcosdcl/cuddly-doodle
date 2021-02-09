import sys
sys.path.append('')

import pytest
from models.product_model import ProductModel


@pytest.fixture
def create_instance():
    product = ProductModel(
        '1234567891234', 'Test Name', 'Test Desciption',
        12.1, 12.1, 12.1, 12.1, 12.1
    )
    return product


def test_instance(create_instance):
    assert isinstance(create_instance, ProductModel)


def test_contructor(create_instance):
    product = create_instance
    assert product.sku is '1234567891234'
    assert product.name is 'Test Name'
    assert product.description is 'Test Desciption'
    assert product.price is 12.1
    assert product.height is 12.1
    assert product.width is 12.1
    assert product.length is 12.1
    assert product.weight is 12.1


@pytest.mark.parametrize("sku, name, description, price, height, \
    width, length, weight", [
    (10, 'Test Name', 'Test Desciption',
        12.1, 12.1, 12.1, 12.1, 12.1),
    (10.5, 'Test Name', 'Test Desciption',
        12.1, 12.1, 12.1, 12.1, 12.1),
    (False, 'Test Name', 'Test Desciption',
        12.1, 12.1, 12.1, 12.1, 12.1)
])
def test_sku_type_exception(sku, name, description, price, 
                                height, width, length, weight):
    with pytest.raises(TypeError):
        product = ProductModel(sku, name, description, price, 
                                height, width, length, weight)


@pytest.mark.parametrize("sku, name, description, price, height, \
    width, length, weight", [
    ('1234567891234', 10, 'Test Desciption',
        12.1, 12.1, 12.1, 12.1, 12.1),
    ('1234567891234', True, 'Test Desciption',
        12.1, 12.1, 12.1, 12.1, 12.1),
    ('1234567891234', None, 'Test Desciption',
        12.1, 12.1, 12.1, 12.1, 12.1)
])
def test_name_type_exception(sku, name, description, price, 
                                height, width, length, weight):
    with pytest.raises(TypeError):
        product = ProductModel(sku, name, description, price, 
                                height, width, length, weight)


@pytest.mark.parametrize("sku, name, description, price, height, \
    width, length, weight", [
    ('1234567891234', 'Test Name', False,
        12.1, 12.1, 12.1, 12.1, 12.1),
    ('1234567891234', 'Test Name', 20,
        12.1, 12.1, 12.1, 12.1, 12.1),
    ('1234567891234', 'Test Name', None,
        12.1, 12.1, 12.1, 12.1, 12.1)
])
def test_description_type_exception(sku, name, description, price, 
                                        height, width, length, weight):
    with pytest.raises(TypeError):
        product = ProductModel(sku, name, description, price, 
                                height, width, length, weight)

@pytest.mark.parametrize("sku, name, description, price, height, \
    width, length, weight", [
    ('1234567891234', 'Test Name', 'Test Desciption',
        None, 12.1, 12.1, 12.1, 12.1),
    ('1234567891234', 'Test Name', 'Test Desciption',
        '12.1', 12.1, 12.1, 12.1, 12.1),
    ('1234567891234', 'Test Name', 'Test Desciption',
        12, 12.1, 12.1, 12.1, 12.1)
])
def test_price_type_exception(sku, name, description, price, 
                                        height, width, length, weight):
    with pytest.raises(TypeError):
        product = ProductModel(sku, name, description, price, 
                                height, width, length, weight)


@pytest.mark.parametrize("sku, name, description, price, height, \
    width, length, weight", [
    ('1234567891234', 'Test Name', 'Test Desciption',
        12.1, None, 12.1, 12.1, 12.1),
    ('1234567891234', 'Test Name', 'Test Desciption',
        12.1, False, 12.1, 12.1, 12.1),
    ('1234567891234', 'Test Name', 'Test Desciption',
        12.1, '12.1', 12.1, 12.1, 12.1)
])
def test_height_type_exception(sku, name, description, price, 
                                        height, width, length, weight):
    with pytest.raises(TypeError):
        product = ProductModel(sku, name, description, price, 
                                height, width, length, weight)


@pytest.mark.parametrize("sku, name, description, price, height, \
    width, length, weight", [
    ('1234567891234', 'Test Name', 'Test Desciption',
        12.1, 12.1, None, 12.1, 12.1),
    ('1234567891234', 'Test Name', 'Test Desciption',
        12.1, 12.1, '12.1', 12.1, 12.1),
    ('1234567891234', 'Test Name', 'Test Desciption',
        12.1, 12.1, 10, 12.1, 12.1)
])
def test_width_type_exception(sku, name, description, price, 
                                        height, width, length, weight):
    with pytest.raises(TypeError):
        product = ProductModel(sku, name, description, price, 
                                height, width, length, weight)


@pytest.mark.parametrize("sku, name, description, price, height, \
    width, length, weight", [
    ('1234567891234', 'Test Name', 'Test Desciption',
        12.1, 12.1, 12.1, False, 12.1),
    ('1234567891234', 'Test Name', 'Test Desciption',
        12.1, 12.1, 12.1, 1, 12.1),
    ('1234567891234', 'Test Name', 'Test Desciption',
        12.1, 12.1, 10.1, None, 12.1)
])
def test_length_type_exception(sku, name, description, price, 
                                        height, width, length, weight):
    with pytest.raises(TypeError):
        product = ProductModel(sku, name, description, price, 
                                height, width, length, weight)


@pytest.mark.parametrize("sku, name, description, price, height, \
    width, length, weight", [
    ('1234567891234', 'Test Name', 'Test Desciption',
        12.1, 12.1, 12.1, 12.1, '12.1'),
    ('1234567891234', 'Test Name', 'Test Desciption',
        12.1, 12.1, 12.1, 1.1, False),
    ('1234567891234', 'Test Name', 'Test Desciption',
        12.1, 12.1, 10.1, 12.1, None)
])
def test_weight_type_exception(sku, name, description, price, 
                                        height, width, length, weight):
    with pytest.raises(TypeError):
        product = ProductModel(sku, name, description, price, 
                                height, width, length, weight)


def test_sku_value_exception():
    with pytest.raises(ValueError):
        product = ProductModel('12345678912', 'Test Name', 'Test Desciption',
                                12.1, 12.1, 12.1, 12.1, 12.1)


def test_name_empty_exception():
    with pytest.raises(ValueError):
        product = ProductModel('1234567891234', ' ', 'Test Desciption',
                                12.1, 12.1, 12.1, 12.1, 12.1)


def test_description_empty_exception():
    with pytest.raises(ValueError):
        product = ProductModel('1234567891234', 'Test Name', '   ',
                                12.1, 12.1, 12.1, 12.1, 12.1)


def test_name_max_len_exception():
    with pytest.raises(ValueError):
        product = ProductModel('1234567891234', 'i'*101, 'Test Desciption',
                                12.1, 12.1, 12.1, 12.1, 12.1)


def test_description_max_len_exception():
    with pytest.raises(ValueError):
        product = ProductModel('1234567891234', 'Test Name', 'i'*256,
                                12.1, 12.1, 12.1, 12.1, 12.1)


def test_price_zero_exception():
    with pytest.raises(ValueError):
        product = ProductModel('1234567891234', 'Test Name', 'Test Description',
                                0.0, 12.1, 12.1, 12.1, 12.1)

def test_height_zero_exception():
    with pytest.raises(ValueError):
        product = ProductModel('1234567891234', 'Test Name', 'Test Description',
                                1.0, 0.0, 12.1, 12.1, 12.1)


def test_width_zero_exception():
    with pytest.raises(ValueError):
        product = ProductModel('1234567891234', 'Test Name', 'Test Description',
                                1.0, 1.0, 0.0, 12.1, 12.1)


def test_length_zero_exception():
    with pytest.raises(ValueError):
        product = ProductModel('1234567891234', 'Test Name', 'Test Description',
                                1.0, 1.0, 1.0, 0.0, 12.1)


def test_weight_zero_exception():
    with pytest.raises(ValueError):
        product = ProductModel('1234567891234', 'Test Name', 'Test Description',
                                1.0, 1.0, 1.0, 1.0, 0.0)
