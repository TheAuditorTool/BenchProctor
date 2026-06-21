# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63994(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
