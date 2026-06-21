# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77885(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
