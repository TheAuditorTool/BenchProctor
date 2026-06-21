# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19199(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
