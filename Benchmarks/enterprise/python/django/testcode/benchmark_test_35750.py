# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest35750(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    return HttpResponse(Template(origin_value).render(Context()))
