# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10534(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
