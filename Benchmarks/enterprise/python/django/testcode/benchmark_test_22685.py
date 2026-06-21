# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22685(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if not str(header_value).isdigit():
        raise ValueError('invalid input: ' + str(header_value))
    return JsonResponse({"saved": True})
