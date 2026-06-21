# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48737(request):
    raw_body = request.body.decode('utf-8')
    try:
        result = int(str(raw_body))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
