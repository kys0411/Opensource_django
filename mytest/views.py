from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question

user_answer = {}


def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'mytest/index.html', context)


def test(request, id):
    if request.POST:
        user_answer[id] = request.POST['correct']
        return redirect("/")
    question = get_object_or_404(Question, pk=id)
    return render(request, 'mytest/test.html', {'question': question})


def result(request, id):
    question = get_object_or_404(Question, pk=id)
    is_result = True
    answer_result = True

    if user_answer.get(id, -1) != -1:
        if user_answer[id] == str(question.correct):
            answer_result = True
        else:
            answer_result = False
    else:
        is_result= False

    return render(request, 'mytest/result.html', {'answer_result': answer_result,
                                                  'question': question,
                                                  'is_result' : is_result})

def stats(request):
    question_list = Question.objects.all()
    question_count = len(question_list)
    result_list = []
    correct_count = 0
    correct_rate = 0
    isStats = True
    if len(user_answer) == question_count:
        for question in question_list:
            if user_answer[question.id] == str(question.correct):
                result_list.append(True)
                correct_count += 1
            else:
                result_list.append(False)
        correct_rate = round(correct_count * 100 / question_count, 2)
    else:
        isStats= False

    return render(request, 'mytest/stats.html', {'question_list': question_list,
                                                 'result_list': result_list,
                                                 'question_count': question_count,
                                                 'correct_count': correct_count,
                                                 'correct_rate': correct_rate,
                                                 'isStats': isStats})

