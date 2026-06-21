# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15477(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
