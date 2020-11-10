import pytest
from students.models import Course
from model_bakery import baker


@pytest.fixture()
def course_factory():
    # просто создать и вернуть сущность нельзя - нужны детали!
    #
    def factory(**kwargs):
        #указываем "app.Модель"
        course=baker.make("students.Course", **kwargs)
        return course

    return factory

@pytest.fixture()
def student_factory():
    # просто создать и вернуть сущность нельзя - нужны детали!
    #
    def factory(**kwargs):
        #указываем "app.Модель"
        student=baker.make("students.Student", **kwargs)
        return student

    return factory