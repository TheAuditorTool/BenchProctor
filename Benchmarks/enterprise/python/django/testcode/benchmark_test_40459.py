# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40459(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
