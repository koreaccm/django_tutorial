# Create your views here.
from django.template import Context, loader, RequestContext
from polls.models import Poll, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
"""
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

    #t = loader.get_template('polls/index.html')
    #c = Context({
                 'latest_poll_list': latest_poll_list,
                 })
    #return HttpResponse(t.render(c))
"""
#from django.http import Http404    
"""
def detail(request, poll_id):
    
    p = get_object_or_404(Poll, pk=poll_id)
    
    #try:
    #    p = Poll.objects.get(pk=poll_id)
    #except Poll.DoesNotExist:
    #    raise Http404
    
    return render_to_response('polls/detail.html', {'poll': p}, context_instance=RequestContext(request))
    #return HttpResponse("You're looking at poll %s." % poll_id)
"""

"""
def results(request, poll_id):
    #return HttpResponse("You're looking at the results of poll %s." % poll_id)
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': p}) 
"""

def vote(request, poll_id):
    #return HttpResponse("You're voting on poll %s." % poll_id)
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render_to_response('polls/detail.html', {
            'poll': p, 
            'error_message': "You didn't select a choice",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
        
    
    
    
