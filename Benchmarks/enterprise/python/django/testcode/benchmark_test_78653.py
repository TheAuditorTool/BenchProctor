# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import time


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest78653(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = default_blank(forwarded_ip)
    if time.time() > 1000000000:
        return HttpResponse(Template(data).render(Context()))
    return JsonResponse({"saved": True})
