# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07885(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
