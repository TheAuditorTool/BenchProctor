# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43593(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
