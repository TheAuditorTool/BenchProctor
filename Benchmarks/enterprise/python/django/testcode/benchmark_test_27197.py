# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27197(request):
    raw_body = request.body.decode('utf-8')
    pending = list(str(raw_body).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
