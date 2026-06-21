# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16876(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = str(origin_value).replace('\x00', '')
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
