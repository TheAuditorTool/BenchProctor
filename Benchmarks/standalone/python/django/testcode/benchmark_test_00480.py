# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from app_runtime import db


def BenchmarkTest00480(request):
    user_id = request.GET.get('id', '')
    parts = str(user_id).split(',')
    data = ' '.join(parts)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    db.execute('SELECT * FROM users ORDER BY ' + str(processed))
    return JsonResponse({"saved": True})
