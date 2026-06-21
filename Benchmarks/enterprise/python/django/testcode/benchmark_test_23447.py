# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23447(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
