# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest69753(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    prefix = ''
    data = prefix + str(ua_value)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
