# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00329(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = []
    for token in str(comment_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
