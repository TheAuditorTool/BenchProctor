# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06873(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
