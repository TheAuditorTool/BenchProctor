# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64915(request):
    upload_name = request.FILES['upload'].name
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
