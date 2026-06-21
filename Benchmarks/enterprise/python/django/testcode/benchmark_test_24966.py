# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24966(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
