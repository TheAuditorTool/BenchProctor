# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


def BenchmarkTest48684(request):
    raw_body = request.body.decode('utf-8')
    pending = list(str(raw_body).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
