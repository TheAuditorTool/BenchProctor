# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18669(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
