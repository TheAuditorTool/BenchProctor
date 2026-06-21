# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest15749(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
