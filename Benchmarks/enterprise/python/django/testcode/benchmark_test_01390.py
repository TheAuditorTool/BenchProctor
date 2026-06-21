# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest01390(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    return HttpResponse(Template(header_value).render(Context()))
