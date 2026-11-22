# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.core.cache import cache
import re
from app_runtime import db


def BenchmarkTest00014(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    cache.set('active_tenant', str(processed), None)
    return JsonResponse({"saved": True})
