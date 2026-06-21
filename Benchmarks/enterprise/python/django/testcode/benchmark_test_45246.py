# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import os


def BenchmarkTest45246(request):
    env_value = os.environ.get('USER_INPUT', '')
    random.seed(int(env_value) if str(env_value).isdigit() else 7)
    token = random.getrandbits(8)
    return JsonResponse({'token': str(token)}, status=200)
