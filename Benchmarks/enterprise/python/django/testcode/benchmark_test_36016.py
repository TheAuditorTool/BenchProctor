# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36016(request):
    upload_name = request.FILES['upload'].name
    pending = list(str(upload_name).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
