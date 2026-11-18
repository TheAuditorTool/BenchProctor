# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from pathlib import Path


def BenchmarkTest00032(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = '%s' % (env_value,)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = str(candidate)
    os.unlink(checked_path)
    return JsonResponse({"saved": True})
