# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import pickle


def BenchmarkTest67569(request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
