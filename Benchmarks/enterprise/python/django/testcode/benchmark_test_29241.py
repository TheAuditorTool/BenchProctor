# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def BenchmarkTest29241(request):
    raw_body = request.body.decode('utf-8')
    pending = list(str(raw_body).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
