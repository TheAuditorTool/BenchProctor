# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06187(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    exec(str(data))
    return JsonResponse({"saved": True})
