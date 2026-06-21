# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00326(request):
    upload_name = request.FILES['upload'].name
    data, _sep, _rest = str(upload_name).partition('\x00')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
