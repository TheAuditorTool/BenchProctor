# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56348(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
