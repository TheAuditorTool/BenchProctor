# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import numpy as np
from app_runtime import db


def BenchmarkTest00195(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(comment_value)
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _bounded
    quantity = int(processed)
    total_cents = np.int64(min(quantity, 100000)) * np.int64(1999)
    return JsonResponse({'total_cents': int(total_cents)}, status=200)
