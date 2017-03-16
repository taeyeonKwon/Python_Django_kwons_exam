from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from polls.models import Question, Choice

# Create your views here.

# index() 변동없음
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# detail() 변동없음
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html',{'question':question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice - p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        #설문 투표 폼을 다시 보여준다
        return render(request, 'polls/detail.html',{
            'question':p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        # POST데이터를 정상적으로 처리했다면
        # 항상 HttpResponseRedirect를 반환하여 리다이렉션처리한다
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))

def result(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})
