# -*- coding: utf-8 -*-

# todo: 1) Разверните репозиторий со своим проектом в директорию /home/box
#       2) В файле qa/forms.py  создайте следующие формы для добавления вопроса и ответа.
#           AskForm - форма добавления вопроса
#           title - поле заголовка
#           text - поле текста вопроса
#           AnswerForm - форма добавления ответа
#           text - поле текста ответа
#           question - поле для связи с вопросом
#       Имена классов форм и полей важны! Конструкторы форм должны получать стандартные для Django-форм аргументы,
#       т.е. должна быть возможность создать объект формы как AskForm() или AnswerForm().
#       На данном этапе формы могут не учитывать авторизацию пользователей,
#       т.е. создавать вопросы и ответы с произвольным либо пустым автором.
#       В формах реализуйте необходимые методы для валидации и сохранения данных (clean и save)
#       3) Создайте view и шаблоны для отображения и сохранения форм
#       URL = /ask/
#   При GET запросе - отображается форма AskForm, при POST запросе форма должна создавать новый вопрос
#   и перенаправлять на страницу вопроса - /question/123/
#   URL = /question/123/
#   При GET запросе должна отображаться страница ответа и на ней AnswerForm.
#   Форма  AnswerForm должна отправлять данные на /question/123/ POST запросом.
#   При POST запросе форма AnswerForm добавляет новый ответ и перенаправляет на страницу вопроса /question/123/.
#   Для поддержки CSRF защиты - выведите в шаблонах форм {% csrf_token %}.
from django import forms


class AskForm(forms.Form):
    pass

class AnswerForm(forms.Form):
    pass
