from django.shortcuts import get_object_or_404, render
from django.http import Http404

# Create your views here.
from django.http import HttpResponse

from .models import Question
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

def view(request):
    return render(request, 'Whoami.html')

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

"""
def vote(request, question_id):
    model = Question
    template_name = 'polls/results.html'
"""
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Soru oylama formunu tekrar göster
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST verileriyle başarılı bir şekilde ilgilendikten sonra
        # daima bir HttpResponseRedirect döndürün. Bu, bir kullanıcı
        # geri düğmesine basarsa verilerin iki kez gönderilmesini önler.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

