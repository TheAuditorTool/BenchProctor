# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38979(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    int(str(data))
    return JsonResponse({"saved": True})
