# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12201(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
