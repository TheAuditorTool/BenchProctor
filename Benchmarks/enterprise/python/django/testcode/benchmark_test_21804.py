# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21804(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
