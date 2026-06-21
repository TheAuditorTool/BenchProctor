# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest41798(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not db_value.lower().endswith(allowed_ext):
        return JsonResponse({'error': 'invalid file type'}, status=400)
    entry_file = os.path.basename(db_value)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
