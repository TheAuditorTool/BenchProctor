# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00678(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
