# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def relay_value(value):
    return value

def BenchmarkTest04216(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = relay_value(referer_value)
    processed = data[:64]
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
