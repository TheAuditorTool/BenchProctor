# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54058(request):
    raw_body = request.body.decode('utf-8')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(raw_body)})
