# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00412(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _bounded
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return JsonResponse({'allocated': allocated}, status=200)
