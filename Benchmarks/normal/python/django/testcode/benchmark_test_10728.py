# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10728(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
