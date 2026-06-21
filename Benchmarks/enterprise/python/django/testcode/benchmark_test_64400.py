# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest64400(request):
    env_value = os.environ.get('USER_INPUT', '')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if env_value not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + env_value
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
