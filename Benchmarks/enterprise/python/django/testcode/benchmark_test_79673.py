# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest79673(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = default_blank(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        return HttpResponse(Template(data).render(Context()))
    return JsonResponse({"saved": True})
