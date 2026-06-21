# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58787(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
