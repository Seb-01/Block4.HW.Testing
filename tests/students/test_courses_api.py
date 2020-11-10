# def test_example():
#     assert False, "Just test example"
import pytest

from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.test import APIClient

from students.models import Course
from tests.students.conftest import course_factory


@pytest.mark.django_db
def test_api_get_courses(api_client, course_factory):

    # arrange
    # класс для создания запросов, имитирующих работу API приложения
    #client = APIClient()
    #GET - list
    #POST - create
    course_factory(name='Pytest for dummies')
    course_factory(name='Pytest for dummies 2')
    course_factory(name='Pytest for dummies 3')

    url=reverse("courses-list")

    # act
    resp=api_client.get(url)

    #assert
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    #если данные есть
    if resp_json != []:
        num_json = len(resp_json)
        assert num_json == 3


@pytest.mark.django_db
def test_api_get_course_num(api_client, course_factory):

    # arrange
    #GET - retrieve
    #DELETE - destroy
    #создаем сущности
    courses=course_factory(name='Pytest for dummies')
    #формируем url вида: '/api/v1/courses/1/'
    url=reverse("courses-detail", args=(courses.id, ))

    # act
    resp=api_client.get(url)

    #assert
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    #если данные есть
    if resp_json != []:
        st_t = resp_json["name"]
        assert st_t == "Pytest for dummies"

@pytest.mark.django_db
def test_api_get_course_filter_id(api_client, course_factory):

    # arrange
    # класс для создания запросов, имитирующих работу API приложения
    #client = APIClient()
    #GET - retrieve
    #DELETE - destroy
    #создаем три сущности
    course1=course_factory(name='Pytest for dummies 1')
    course2=course_factory(name='Pytest for dummies 2')
    course3=course_factory(name='Pytest for dummies 3')

    url = reverse("courses-list")

    # act
    # Передаем GET-запрос
    resp = api_client.get(url, {"id": [course1.id,course3.id]})

    #assert
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    #если данные есть
    if resp_json != []:
        assert len(resp_json) == 2

@pytest.mark.django_db
def test_api_get_course_filter_name(api_client, course_factory):

    # arrange
    # класс для создания запросов, имитирующих работу API приложения
    #client = APIClient()
    #GET - retrieve
    #DELETE - destroy
    #создаем три сущности
    course_factory(name='Pytest for dummies 1')
    course_factory(name='C# for advanced levels prof')
    course_factory(name='C++ for dummies 3')

    url = reverse("courses-list")

    # act
    # Передаем GET-запрос
    resp = api_client.get(url, {"name": ['C# for advanced levels prof']})

    #assert
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    #если данные есть
    if resp_json != []:
        st_t = resp_json[0]["name"]
        assert st_t == "C# for advanced levels prof"


@pytest.mark.django_db
def test_api_create_course(api_client):

    # arrange
    url = reverse("courses-list")
    product_payload = {
        "name": "C# for advanced levels prof",
    }

    # act
    # Передаем POST-запрос
    resp = api_client.post(url,product_payload)

    #assert
    assert resp.status_code == HTTP_201_CREATED
    assert resp.status_text == 'Created'

@pytest.mark.django_db
def test_api_update_course(api_client, course_factory):

    # arrange
    courses1=course_factory(name='Pytest for dummies 1')
    courses2=course_factory(name='C# for advanced levels prof')
    courses3=course_factory(name='C++ for dummies 3')

    url=reverse("courses-detail", args=(courses2.id, ))
    product_payload = {
        "name": "C# only for very advanced levels profi!",
    }

    # act
    # Передаем POST-запрос
    resp = api_client.put(url,product_payload)

    #assert
    assert resp.status_code == HTTP_200_OK
    assert resp.status_text == 'OK'

    resp_json = resp.json()
    # если данные есть
    if resp_json != []:
        st_t = resp_json["name"]
        assert st_t == "C# only for very advanced levels profi!"

@pytest.mark.django_db
def test_api_delete_course(api_client, course_factory):

    # arrange
    courses1=course_factory(name='Pytest for dummies 1')
    courses2=course_factory(name='C# for advanced levels prof')
    courses3=course_factory(name='C++ for dummies 3')

    url=reverse("courses-detail", args=(courses2.id, ))

    # act
    # Передаем POST-запрос
    resp = api_client.delete(url)

    #assert
    assert resp.status_code == HTTP_204_NO_CONTENT
    assert resp.status_text == 'No Content'

