# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53428(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
