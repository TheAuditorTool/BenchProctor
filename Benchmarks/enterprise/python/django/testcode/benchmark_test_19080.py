# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19080(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
