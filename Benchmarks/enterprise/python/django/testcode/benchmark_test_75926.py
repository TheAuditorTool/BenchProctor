# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest75926(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    processed = data[:64]
    return JsonResponse({'error': str(processed), 'stack': repr(locals())}, status=500)
