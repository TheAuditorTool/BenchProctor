# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10222(request):
    upload_name = request.FILES['upload'].name
    size = min(int(upload_name) if str(upload_name).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
