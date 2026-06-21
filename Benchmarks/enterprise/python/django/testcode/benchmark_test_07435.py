# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07435(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
