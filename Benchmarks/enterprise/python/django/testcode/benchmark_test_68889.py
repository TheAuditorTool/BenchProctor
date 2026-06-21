# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest68889(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
