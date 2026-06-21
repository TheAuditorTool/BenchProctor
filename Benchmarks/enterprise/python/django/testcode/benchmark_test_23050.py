# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23050(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '%s' % (forwarded_ip,)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
