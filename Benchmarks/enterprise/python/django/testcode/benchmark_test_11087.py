# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11087(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
