# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest00243(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    pending = list(str(ua_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
