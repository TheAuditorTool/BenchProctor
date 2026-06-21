# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45623(request):
    multipart_value = request.POST.get('multipart_field', '')
    pending = list(str(multipart_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
