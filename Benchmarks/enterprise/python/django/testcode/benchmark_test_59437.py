# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59437(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '%s' % str(forwarded_ip)
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
