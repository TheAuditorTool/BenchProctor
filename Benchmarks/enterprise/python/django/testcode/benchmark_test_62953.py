# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62953(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
