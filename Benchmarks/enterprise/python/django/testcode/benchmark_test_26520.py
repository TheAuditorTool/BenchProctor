# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26520(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
