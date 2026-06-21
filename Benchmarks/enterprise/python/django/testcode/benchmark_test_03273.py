# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest03273(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = '%s' % str(dotenv_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
