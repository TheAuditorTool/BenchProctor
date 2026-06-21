# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
import os


def BenchmarkTest19103(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
    return JsonResponse({"saved": True})
