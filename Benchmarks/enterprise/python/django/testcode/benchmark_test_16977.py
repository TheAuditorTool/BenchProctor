# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest16977(request):
    cookie_value = request.COOKIES.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
