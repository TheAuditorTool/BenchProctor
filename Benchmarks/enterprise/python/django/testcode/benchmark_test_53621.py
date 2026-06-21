# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from urllib.parse import unquote


def BenchmarkTest53621(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
