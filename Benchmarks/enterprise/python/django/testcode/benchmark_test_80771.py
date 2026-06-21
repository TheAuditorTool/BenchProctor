# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest80771(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    reader = make_reader(ua_value)
    data = reader()
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
