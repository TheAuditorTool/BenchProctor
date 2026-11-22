# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import numpy as np
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00226(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    form = FormData(payload=json_value)
    data = form.payload
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _bounded
    quantity = int(processed)
    total_cents = np.int64(min(quantity, 100000)) * np.int64(1999)
    return JsonResponse({'total_cents': int(total_cents)}, status=200)
