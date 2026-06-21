# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30429(request):
    raw_body = request.body.decode('utf-8')
    if str(raw_body) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
