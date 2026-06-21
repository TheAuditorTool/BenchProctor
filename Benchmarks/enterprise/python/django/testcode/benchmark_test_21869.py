# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest21869(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
