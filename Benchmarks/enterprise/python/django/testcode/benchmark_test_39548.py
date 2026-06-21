# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest39548(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    reader = make_reader(dotenv_value)
    data = reader()
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
