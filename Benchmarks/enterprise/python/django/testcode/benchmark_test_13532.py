# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13532(request):
    raw_body = request.body.decode('utf-8')
    prefix = ''
    data = prefix + str(raw_body)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
