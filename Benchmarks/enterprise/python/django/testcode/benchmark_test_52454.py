# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach
from urllib.parse import unquote


def BenchmarkTest52454(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    processed = bleach.clean(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
