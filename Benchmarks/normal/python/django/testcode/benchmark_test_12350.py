# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12350(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
