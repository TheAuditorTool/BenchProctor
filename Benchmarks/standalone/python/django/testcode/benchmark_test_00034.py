# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from app_runtime import db


def BenchmarkTest00034(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = auth_header if auth_header else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    db.execute('SELECT * FROM users ORDER BY ' + str(processed))
    return JsonResponse({"saved": True})
