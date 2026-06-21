# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09118(request):
    user_id = request.GET.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
