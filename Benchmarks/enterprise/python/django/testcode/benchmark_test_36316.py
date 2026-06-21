# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36316(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
