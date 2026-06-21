# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import os


def BenchmarkTest43953(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
    return JsonResponse({"saved": True})
