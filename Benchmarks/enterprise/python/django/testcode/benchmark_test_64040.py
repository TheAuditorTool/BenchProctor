# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64040(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = bytearray(int(auth_header) if str(auth_header).isdigit() else 0)
    return JsonResponse({"saved": True})
