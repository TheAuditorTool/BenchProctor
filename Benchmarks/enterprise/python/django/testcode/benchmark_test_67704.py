# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from urllib.parse import unquote


def BenchmarkTest67704(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
