# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest36748(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
