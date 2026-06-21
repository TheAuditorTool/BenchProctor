# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path
from dataclasses import dataclass
import sys


@dataclass
class FormData:
    payload: str

def BenchmarkTest00262(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = FormData(payload=argv_value).payload
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = str(candidate)
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
