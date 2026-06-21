# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25791(request):
    raw_body = request.body.decode('utf-8')
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
