# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import numpy as np
from app_runtime import db


def BenchmarkTest00021(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    quantity = int(str(data))
    total_cents = np.int32(quantity) * np.int32(1999)
    return JsonResponse({'total_cents': int(total_cents)}, status=200)
