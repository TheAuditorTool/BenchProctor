# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53411(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
