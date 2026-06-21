# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest09640(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
