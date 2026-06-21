# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59300(request):
    raw_body = request.body.decode('utf-8')
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    eval(str(data))
    return JsonResponse({"saved": True})
