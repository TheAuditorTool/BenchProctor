# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import time


def BenchmarkTest12324(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    if time.time() > 1000000000:
        return HttpResponse(Template(data).render(Context()))
    return JsonResponse({"saved": True})
