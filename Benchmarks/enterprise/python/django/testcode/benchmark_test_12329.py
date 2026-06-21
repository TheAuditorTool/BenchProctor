# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12329(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = (lambda v: v.strip())(header_value)
    int(str(data))
    return JsonResponse({"saved": True})
