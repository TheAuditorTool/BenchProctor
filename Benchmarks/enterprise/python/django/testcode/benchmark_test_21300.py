# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from app_runtime import db


def BenchmarkTest21300(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', auth_header):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = auth_header
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return JsonResponse({"saved": True})
