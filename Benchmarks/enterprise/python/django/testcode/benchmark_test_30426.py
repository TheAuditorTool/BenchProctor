# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
import sys


def BenchmarkTest30426(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    parts = []
    for token in str(argv_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
