# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76883(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    pending = list(str(ua_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
