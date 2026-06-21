# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest72855(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    def normalize(value):
        return value.strip()
    data = normalize(dotenv_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
