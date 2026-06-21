# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest65608(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    reader = make_reader(secret_value)
    data = reader()
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(data)})
    return JsonResponse({"saved": True})
