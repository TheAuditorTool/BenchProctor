# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest09857(request):
    host_value = request.META.get('HTTP_HOST', '')
    return HttpResponse(Template(host_value).render(Context()))
