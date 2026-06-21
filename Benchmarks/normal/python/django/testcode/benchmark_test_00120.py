# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00120(request):
    env_value = os.environ.get('USER_INPUT', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(env_value), secure=True, httponly=True, samesite='Strict')
    return resp
