# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42265(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    prefix = ''
    data = prefix + str(header_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
