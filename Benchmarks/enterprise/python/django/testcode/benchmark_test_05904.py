# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05904(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = ' '.join(str(header_value).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
