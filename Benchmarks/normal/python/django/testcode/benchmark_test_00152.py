# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00152(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
