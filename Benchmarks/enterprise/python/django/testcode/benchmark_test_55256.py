# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55256(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
