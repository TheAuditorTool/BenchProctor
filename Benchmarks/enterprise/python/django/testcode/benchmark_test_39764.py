# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39764(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    eval(str(header_value))
    return JsonResponse({"saved": True})
