# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58185(request):
    user_id = request.GET.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
