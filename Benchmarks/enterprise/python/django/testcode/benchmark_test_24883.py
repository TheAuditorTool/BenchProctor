# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24883(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if str(forwarded_ip).startswith(('10.', '192.168.', '127.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
