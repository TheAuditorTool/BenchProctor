# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77520(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
