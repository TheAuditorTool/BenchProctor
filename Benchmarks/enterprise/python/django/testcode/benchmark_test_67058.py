# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67058(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = str(header_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
