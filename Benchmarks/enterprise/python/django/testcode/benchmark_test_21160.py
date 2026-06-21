# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21160(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = f'{header_value}'
    int(str(data))
    return JsonResponse({"saved": True})
