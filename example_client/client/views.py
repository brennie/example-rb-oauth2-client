"""Client views."""

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.context import RequestContext
from django.template.loader import get_template


def index(request):
    template = get_template('client/index.html')

    return HttpResponse(content=template.render(request=request))


def profile(request):
    if not request.user.is_authenticated():
        return redirect(reverse('index'))

    template = get_template('client/profile.html')
    return HttpResponse(content=template.render(request=request))
