# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest79885(request):
    cookie_value = request.COOKIES.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    requests.get(str(data))
    return JsonResponse({"saved": True})
