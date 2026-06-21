# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43008(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    int(str(data))
    return JsonResponse({"saved": True})
