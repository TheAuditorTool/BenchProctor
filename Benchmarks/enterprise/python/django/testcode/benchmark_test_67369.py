# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67369(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    prefix = ''
    data = prefix + str(origin_value)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
