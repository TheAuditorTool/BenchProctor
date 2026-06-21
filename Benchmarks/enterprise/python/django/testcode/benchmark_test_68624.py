# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import base64
from django.template import Template, Context


def BenchmarkTest68624(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    return HttpResponse(Template('{{ value }}').render(Context({'value': data})))
