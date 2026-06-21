# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12548(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % str(auth_header)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
