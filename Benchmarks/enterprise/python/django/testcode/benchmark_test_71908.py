# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71908(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = str(header_value).replace('\x00', '')
    if str(data).startswith(('10.', '192.168.', '127.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
