# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import numpy as np
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00011(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _bounded
    quantity = int(processed)
    total_cents = np.int64(min(quantity, 100000)) * np.int64(1999)
    return JsonResponse({'total_cents': int(total_cents)}, status=200)
