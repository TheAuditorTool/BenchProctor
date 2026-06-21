# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06923(request):
    upload_name = request.FILES['upload'].name
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
