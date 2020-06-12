from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime



def index(request):
    return render(request, 'index.html', {'Test': "Placeholder"})


# def add_request(request, deleted=''):
#     animal = get_object_or_404(Animals, pk=animal_id)
#     if deleted:
#         animal.delete()
#     return render(request, 'polls/detail.html', {'': poll, 'deleted': deleted})

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


