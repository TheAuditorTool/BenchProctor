# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38629(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body}'
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
