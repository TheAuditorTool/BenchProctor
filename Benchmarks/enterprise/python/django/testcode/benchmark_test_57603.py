# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest57603(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
