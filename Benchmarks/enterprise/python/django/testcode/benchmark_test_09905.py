# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest09905(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = default_blank(cookie_value)
    if os.environ.get("APP_ENV", "production") != "test":
        return HttpResponse(Template(data).render(Context()))
    return JsonResponse({"saved": True})
