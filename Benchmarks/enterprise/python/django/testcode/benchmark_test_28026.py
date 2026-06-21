# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest28026(request):
    env_value = os.environ.get('USER_INPUT', '')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(env_value))
    return JsonResponse({'lookup': arr[idx]}, status=200)
