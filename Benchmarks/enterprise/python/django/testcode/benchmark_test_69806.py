# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69806(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
