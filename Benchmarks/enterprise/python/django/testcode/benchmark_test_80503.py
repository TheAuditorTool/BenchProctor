# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80503(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
