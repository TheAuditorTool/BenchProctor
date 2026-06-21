# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53786(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
