# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12983(request):
    user_id = request.GET.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
