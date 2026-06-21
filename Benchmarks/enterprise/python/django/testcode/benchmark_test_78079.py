# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78079(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
