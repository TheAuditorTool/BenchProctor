# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22175(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
