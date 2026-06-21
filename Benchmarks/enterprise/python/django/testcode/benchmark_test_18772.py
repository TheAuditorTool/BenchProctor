# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18772(request):
    user_id = request.GET.get('id', '')
    if str(user_id) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
