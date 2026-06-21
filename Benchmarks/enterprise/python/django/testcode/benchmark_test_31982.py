# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31982(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = f'{forwarded_ip}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
