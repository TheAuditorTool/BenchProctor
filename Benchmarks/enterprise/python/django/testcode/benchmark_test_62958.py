# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62958(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
