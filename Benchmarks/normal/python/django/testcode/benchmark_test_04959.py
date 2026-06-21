# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04959(request):
    raw_body = request.body.decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
