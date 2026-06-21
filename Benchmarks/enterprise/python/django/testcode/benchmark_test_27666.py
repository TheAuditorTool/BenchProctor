# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path
from app_runtime import db


def BenchmarkTest27666(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = profile_value if profile_value else 'default'
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = str(candidate)
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
