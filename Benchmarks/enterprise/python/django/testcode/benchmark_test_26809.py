# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import os


def BenchmarkTest26809(request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
