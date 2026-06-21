# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02004(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
