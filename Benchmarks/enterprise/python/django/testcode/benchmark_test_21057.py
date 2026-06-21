# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest21057(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = f'{dotenv_value:.200s}'
    request.session.clear()
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
