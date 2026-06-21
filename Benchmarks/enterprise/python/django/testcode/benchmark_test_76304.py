# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76304(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
