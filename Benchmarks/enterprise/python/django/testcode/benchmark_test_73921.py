# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest73921(request):
    upload_name = request.FILES['upload'].name
    data = coalesce_blank(upload_name)
    if not re.fullmatch("^[\\w\\s.'\\\\;_/\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return JsonResponse({"saved": True})
