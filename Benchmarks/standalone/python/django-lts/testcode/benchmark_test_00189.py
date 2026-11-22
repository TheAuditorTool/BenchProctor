# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from pathlib import Path
from app_runtime import db


def BenchmarkTest00189(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = f'{profile_value!s}'
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = full_path
    Path(checked_path).write_text('data')
    return JsonResponse({"saved": True})
