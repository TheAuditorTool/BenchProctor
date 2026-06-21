# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63910(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    if str(data).startswith(('10.', '192.168.', '127.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
