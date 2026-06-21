# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71569(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
