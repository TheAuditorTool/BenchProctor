# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26313(request):
    upload_name = request.FILES['upload'].name
    parts = []
    for token in str(upload_name).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
