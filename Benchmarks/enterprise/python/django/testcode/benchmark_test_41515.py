# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import os


def BenchmarkTest41515(request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return JsonResponse({'token': str(token)}, status=200)
