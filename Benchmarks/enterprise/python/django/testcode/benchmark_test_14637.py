# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path
import os
from django.http import HttpResponse


def ensure_str(value):
    return str(value)

def BenchmarkTest14637(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = str(candidate)
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
