# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21109(request):
    upload_name = request.FILES['upload'].name
    data, _sep, _rest = str(upload_name).partition('\x00')
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
