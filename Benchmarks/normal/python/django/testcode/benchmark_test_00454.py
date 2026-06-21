# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00454(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
