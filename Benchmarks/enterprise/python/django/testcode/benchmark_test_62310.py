# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import pickle


def BenchmarkTest62310(request):
    env_value = os.environ.get('USER_INPUT', '')
    pending = list(str(env_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
