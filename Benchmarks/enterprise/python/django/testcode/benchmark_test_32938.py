# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32938(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
