# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import pickle


def BenchmarkTest00005(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    pickle.loads(base64.b64decode(data))
    return JsonResponse({"saved": True})
