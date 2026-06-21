# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80513(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
