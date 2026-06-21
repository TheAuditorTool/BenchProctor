# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26500(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    if str(data).startswith(('10.', '192.168.', '127.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
