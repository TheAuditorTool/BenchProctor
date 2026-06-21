# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61603(request):
    user_id = request.GET.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
