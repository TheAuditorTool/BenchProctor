# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10862(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
