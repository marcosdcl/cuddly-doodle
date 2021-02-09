import sys
sys.path.append('.')

import pytest
from models.product_model import ProductModel
from dao.base_dao import BaseDao
from dao.product_dao import ProductDao


@pytest.fixture
def create_model():
    product = ProductModel(
        '1234567891234', 'Test Name', 'Test Desciption',
        12.1, 12.1, 12.1, 12.1, 12.1
    )
    return product


@pytest.fixture
def create_dao():
    product_dao = ProductDao()
    return product_dao


def test_instance(create_dao):
    assert isinstance(create_dao, ProductDao)


def test_inheritance(create_dao):
    assert isinstance(create_dao, BaseDao)


def test_save(create_dao, create_model):
    global model
    model = create_dao.save(create_model)
    assert model is create_model


def test_read_all(create_dao):
    rows = create_dao.read_all()
    assert isinstance(rows, list)


def test_read_by_id(create_dao):
    model_ = create_dao.read_by_id(model.id_)
    assert model_ is not None


def test_delete(create_dao):
    create_dao.delete(model)
    model_ = create_dao.read_by_id(model.id_)
    assert model_ is None


def test_read_by_id_type_exception(create_dao):
    with pytest.raises(TypeError):
        model_ = create_dao.read_by_id('asd')
