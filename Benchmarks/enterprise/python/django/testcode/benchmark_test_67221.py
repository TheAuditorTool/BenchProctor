# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest67221(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
