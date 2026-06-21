# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
import sys


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest42453(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = handle(argv_value)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
