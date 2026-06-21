# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path
import os


def BenchmarkTest34947(request):
    env_value = os.environ.get('USER_INPUT', '')
    base = Path('/var/app/data').resolve()
    candidate = (base / env_value).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = str(candidate)
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
