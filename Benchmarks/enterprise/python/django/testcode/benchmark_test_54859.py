# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest54859(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    state = globals().setdefault('_lcg_state', [12345])
    state[0] = (state[0] * 1103515245 + (int(data) if str(data).isdigit() else 1)) % (2 ** 31)
    token = state[0]
    return JsonResponse({'token': str(token)}, status=200)
