# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47155(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(processed)})
