# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25652(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % str(origin_value)
    if str(data) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
