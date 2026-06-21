# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44329(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
