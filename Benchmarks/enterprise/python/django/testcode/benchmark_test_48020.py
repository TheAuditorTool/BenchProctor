# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48020(request):
    upload_name = request.FILES['upload'].name
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
