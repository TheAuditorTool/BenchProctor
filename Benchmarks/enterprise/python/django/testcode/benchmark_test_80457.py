# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80457(request):
    xml_value = request.body.decode('utf-8')
    pending = list(str(xml_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
