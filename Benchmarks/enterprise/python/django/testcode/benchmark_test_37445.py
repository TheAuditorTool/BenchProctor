# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest37445(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(processed)})
