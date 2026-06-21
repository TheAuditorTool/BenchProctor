# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45251(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
