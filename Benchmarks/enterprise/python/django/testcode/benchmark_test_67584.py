# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest67584(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    prefix = ''
    data = prefix + str(ua_value)
    return HttpResponse(Template(data).render(Context()))
