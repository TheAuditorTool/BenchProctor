# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest05687(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
