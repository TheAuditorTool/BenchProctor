# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47185(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
