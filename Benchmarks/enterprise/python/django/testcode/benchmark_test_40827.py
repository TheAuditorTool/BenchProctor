# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40827(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body}'
    try:
        result = int(str(data))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
