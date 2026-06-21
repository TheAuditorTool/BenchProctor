# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49067(request):
    user_id = request.GET.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
