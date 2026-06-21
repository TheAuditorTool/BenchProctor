# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest74617(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    parts = str(dotenv_value).split(',')
    data = ','.join(parts)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
