# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest53666(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    return HttpResponse(Template(data).render(Context()))
