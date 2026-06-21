# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest33291(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ensure_str(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return JsonResponse({"saved": True})
