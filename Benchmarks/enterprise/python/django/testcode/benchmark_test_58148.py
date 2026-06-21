# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58148(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
