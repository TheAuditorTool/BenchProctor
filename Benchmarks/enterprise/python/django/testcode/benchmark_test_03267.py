# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03267(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % str(auth_header)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
