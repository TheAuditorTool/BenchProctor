# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest42127(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
