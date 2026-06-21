# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67677(request):
    multipart_value = request.POST.get('multipart_field', '')
    pending = list(str(multipart_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
