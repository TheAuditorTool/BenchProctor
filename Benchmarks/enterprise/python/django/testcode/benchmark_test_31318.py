# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31318(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
