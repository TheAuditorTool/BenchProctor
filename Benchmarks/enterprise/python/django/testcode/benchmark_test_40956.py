# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import os


def BenchmarkTest40956(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(data) if str(data).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return JsonResponse({'token': str(token)}, status=200)
