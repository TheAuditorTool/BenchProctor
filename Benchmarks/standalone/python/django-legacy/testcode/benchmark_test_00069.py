# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import numpy as np


def BenchmarkTest00069(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _bounded
    quantity = int(processed)
    total_cents = np.int64(min(quantity, 100000)) * np.int64(1999)
    return JsonResponse({'total_cents': int(total_cents)}, status=200)
