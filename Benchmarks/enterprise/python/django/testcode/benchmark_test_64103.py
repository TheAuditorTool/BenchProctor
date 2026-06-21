# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest64103(request):
    xml_value = request.body.decode('utf-8')
    pending = list(str(xml_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    requests.get(str(data))
    return JsonResponse({"saved": True})
