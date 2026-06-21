# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest59264(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    return HttpResponse(mark_safe('<div>' + str(ua_value) + '</div>'))
