# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13598(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = str(header_value).replace('\x00', '')
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
