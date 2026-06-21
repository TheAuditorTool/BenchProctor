# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04288(request):
    raw_body = request.body.decode('utf-8')
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
