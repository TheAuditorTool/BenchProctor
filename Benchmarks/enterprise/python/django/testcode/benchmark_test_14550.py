# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest14550(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
