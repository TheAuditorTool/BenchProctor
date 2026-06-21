# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80971(request):
    xml_value = request.body.decode('utf-8')
    pending = list(str(xml_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    int(str(data))
    return JsonResponse({"saved": True})
