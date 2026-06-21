# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36183(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
