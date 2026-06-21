# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest75851(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
