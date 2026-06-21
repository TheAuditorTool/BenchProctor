# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53260(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % (raw_body,)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
