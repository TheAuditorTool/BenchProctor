# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50324(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
