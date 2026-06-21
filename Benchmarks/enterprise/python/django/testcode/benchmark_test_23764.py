# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest23764(request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
