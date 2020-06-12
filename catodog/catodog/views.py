from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime


def index(request):
    return render(request, 'index.html', {'Test': "Placeholder"})


# def detail(request, poll_id, deleted=''):
#     poll = get_object_or_404(Poll, pk=poll_id)
#     if deleted:
#         poll.delete()
#     return render(request, 'polls/detail.html', {'poll': poll, 'deleted': deleted})

# def vote(request, poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)
#     # try:
#     #     selected_comment = poll.comment_set.get(pk=request.POST['comment'])
#     # except (KeyError, Comment.DoesNotExist):
#     if request.POST['other']:
#         new_comment = poll.comment_set.create(comment_text=request.POST['other'], added_by=request.user)
#         new_comment.save()
#         return HttpResponseRedirect(reverse('polls:detail', args=(poll.id,)))
#         # Redisplay the poll voting form.
#         # return render(request, 'polls/detail.html', {
#         #     'poll': poll,
#         #     'error_message': "You didn't select a comment.",
#         # })
#     # else:
#     #     selected_comment.votes += 1
#     #     selected_comment.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#     return HttpResponseRedirect(reverse('polls:detail', args=(poll.id,)))


# def add_poll(request):
#     submitted = False
#     if request.method == 'POST':
#         form = PollForm(request.POST)
#         if form.is_valid():
#             poll_text = form.cleaned_data['text']
#             poll_title = form.cleaned_data['title']
#             poll = Poll(poll_title = poll_title, poll_text = poll_text, pub_date = datetime.datetime.now())
#             is_anon = request.POST.get('anon', False)
#             if is_anon:
#                 poll.save()
#             else:
#                 if request.user.is_authenticated:
#                     poll.pub_by = request.user
#                 #poll.save()
#             poll.save()

#             return HttpResponseRedirect('?submitted=True')
#     else:
#         form = PollForm()
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request, 'polls/add_poll.html', {'form': form, 'submitted': submitted})
