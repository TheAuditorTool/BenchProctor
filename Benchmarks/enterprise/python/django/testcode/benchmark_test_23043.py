# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23043(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
