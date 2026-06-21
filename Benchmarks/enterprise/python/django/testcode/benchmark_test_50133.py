# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50133(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
