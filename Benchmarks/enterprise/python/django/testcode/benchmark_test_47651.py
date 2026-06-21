# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html


def BenchmarkTest47651(request):
    cookie_value = request.COOKIES.get('session_token', '')
    processed = html.escape(cookie_value)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
