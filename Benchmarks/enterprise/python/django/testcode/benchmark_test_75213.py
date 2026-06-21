# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75213(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if header_value:
        data = header_value
    else:
        data = ''
    eval(str(data))
    return JsonResponse({"saved": True})
