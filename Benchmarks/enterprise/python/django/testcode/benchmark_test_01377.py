# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest01377(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
