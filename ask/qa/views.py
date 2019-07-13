from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .form import AskForm
from .models import Question, Answer
from django.core.paginator import Paginator
from django.db.models import Q


def test(request, *args, **kwargs):
    return HttpResponse('OK')


# Create your views here.

# Главная страница Список "новых" вопросов.
def main(request):
    # Список новых вопросов
    questions_new = Question.objects.new()
    # Ограничение по выводу
    limit = request.GET.get('limit', 10)
    # Создание пагинатора
    paginator = Paginator(questions_new, limit)
    paginator.baseurl = reverse('main')
    # Страница из GET запроса
    page = int(request.GET.get('page', 1))
    page = paginator.page(page)
    return render(request, 'qa/main_new_questions.html',
                  {'paginator': paginator,
                   'page': page})


# Популярные вопросы
def popular(request):
    # Список популярных вопросов
    questions_popular = Question.objects.popular()
    # Ограничение по выводу
    limit = request.GET.get('limit', 10)
    # Создание пагинатора
    paginator = Paginator(questions_popular, limit)
    paginator.baseurl = reverse('popular')
    # Страница из Get запроса
    page = request.GET.get('page', 1)
    page = paginator.page(page)
    return render(request, 'qa/popular_questions.html',
                  {'paginator': paginator,
                   'page': page})


# Детали вопроса
def detail(request, index):
    question = Question.objects.filter(id=index).first()
    if question:
        answers = Answer.objects.all().filter(question__id=index)

        return render(request, 'qa/detail_question.html',
                      {'question': question,
                       'answers': answers})
    else:
        raise Http404


# Форма для вопроса
def add_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url(request)
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/add_ask.html', {'form': form})