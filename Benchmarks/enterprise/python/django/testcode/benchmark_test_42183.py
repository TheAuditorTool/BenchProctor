# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42183(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
