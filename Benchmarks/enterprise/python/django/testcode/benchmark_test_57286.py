# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest57286(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    reader = make_reader(dotenv_value)
    data = reader()
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
