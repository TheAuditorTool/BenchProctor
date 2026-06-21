# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71258(request):
    upload_name = request.FILES['upload'].name
    try:
        result = int(str(upload_name))
    except Exception:
        pass
    return JsonResponse({"saved": True})
