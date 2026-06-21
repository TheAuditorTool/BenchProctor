# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61199(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = f'{header_value}'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
