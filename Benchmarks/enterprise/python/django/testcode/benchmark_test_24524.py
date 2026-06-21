# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24524(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
