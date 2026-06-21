# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75461(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body}'
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return JsonResponse({'error': 'zero division'}, status=400)
    result = 100 / divisor
    return JsonResponse({"saved": True})
