# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def BenchmarkTest71912(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    processed = html.escape(ua_value)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
