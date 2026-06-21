# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36809(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '{}'.format(referer_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
