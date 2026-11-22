# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from pathlib import Path


def BenchmarkTest00172(request, path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = str(candidate)
    os.unlink(checked_path)
    return JsonResponse({"saved": True})
