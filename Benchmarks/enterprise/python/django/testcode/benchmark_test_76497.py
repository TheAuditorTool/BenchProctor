# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76497(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
