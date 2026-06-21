# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69637(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
