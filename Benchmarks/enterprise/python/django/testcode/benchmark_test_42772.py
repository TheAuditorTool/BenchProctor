# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42772(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
