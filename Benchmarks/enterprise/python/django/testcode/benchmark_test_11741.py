# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11741(request):
    upload_name = request.FILES['upload'].name
    data, _sep, _rest = str(upload_name).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
