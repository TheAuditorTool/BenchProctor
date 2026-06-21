# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22180(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
