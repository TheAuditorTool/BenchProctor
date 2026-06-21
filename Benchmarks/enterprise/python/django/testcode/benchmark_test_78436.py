# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78436(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
