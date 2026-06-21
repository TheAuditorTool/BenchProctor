# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45499(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
