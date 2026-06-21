# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61994(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = (lambda v: v.strip())(auth_header)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
