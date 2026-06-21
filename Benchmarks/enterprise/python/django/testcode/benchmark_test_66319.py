# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest66319(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = []
    for token in str(multipart_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return JsonResponse({"saved": True})
