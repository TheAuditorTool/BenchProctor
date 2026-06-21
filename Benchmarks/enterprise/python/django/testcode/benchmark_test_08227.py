# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest08227(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
