# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest09632(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
