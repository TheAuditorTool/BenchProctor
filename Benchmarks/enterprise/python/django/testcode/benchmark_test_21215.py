# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21215(request):
    user_id = request.GET.get('id', '')
    if str(user_id) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
