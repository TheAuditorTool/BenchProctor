# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58948(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = ' '.join(str(header_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
