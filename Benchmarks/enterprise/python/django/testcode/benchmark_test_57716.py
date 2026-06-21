# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from urllib.parse import unquote


def BenchmarkTest57716(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    return HttpResponse(Template(data).render(Context()))
