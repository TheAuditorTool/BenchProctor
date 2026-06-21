# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66541(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
