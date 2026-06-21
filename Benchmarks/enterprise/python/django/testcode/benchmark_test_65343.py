# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65343(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = (lambda v: v.strip())(header_value)
    eval(str(data))
    return JsonResponse({"saved": True})
