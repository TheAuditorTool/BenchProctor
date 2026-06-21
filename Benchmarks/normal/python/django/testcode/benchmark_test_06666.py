# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06666(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % (raw_body,)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
