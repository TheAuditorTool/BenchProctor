# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest46657(request):
    raw_body = request.body.decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
