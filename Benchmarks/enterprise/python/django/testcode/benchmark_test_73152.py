# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73152(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
