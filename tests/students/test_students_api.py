# def test_example():
#     assert False, "Just test example"
import pytest

from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient

from students.models import Course
from tests.students.conftest import course_factory


@pytest.mark.django_db
def test_api_get_students(api_client):

    # arrange
    # класс для создания запросов, имитирующих работу API приложения
    #client = APIClient()
    #GET - list
    #POST - create
    url=reverse("students-list")

    # act
    resp=api_client.get(url)

    #assert
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    #если данные есть
    if resp_json != []:
        st_t = resp_json["status_text"]
        assert st_t == "Ok"


@pytest.mark.django_db
def test_api_get_student_num(api_client, student_factory):

    # arrange
    # класс для создания запросов, имитирующих работу API приложения
    #client = APIClient()
    #GET - retrieve
    #DELETE - destroy
    #создаем сущности
    students1 =student_factory(name='Петров')
    students2 = student_factory(name='Иванов')
    students3 = student_factory(name='Сидоров')
    #формируем url вида: '/api/v1/courses/1/'
    url=reverse("students-detail", args=(students3.id, ))

    # act
    resp=api_client.get(url)

    #assert
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    #если данные есть
    if resp_json != []:
        st_t = resp_json["name"]
        assert st_t == "Сидоров"

