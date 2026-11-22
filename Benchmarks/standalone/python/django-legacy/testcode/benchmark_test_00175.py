# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


def BenchmarkTest00175(request):
    env_value = os.environ.get('APP_INPUT', '')
    pending = list(str(env_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
