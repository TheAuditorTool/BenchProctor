# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02494(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
