# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest52806(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
