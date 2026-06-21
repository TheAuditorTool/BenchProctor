# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04273(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = str(referer_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
