# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12980(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = (lambda v: v.strip())(header_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
