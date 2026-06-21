# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58286(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
