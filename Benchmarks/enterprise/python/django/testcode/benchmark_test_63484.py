# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63484(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body}'
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
