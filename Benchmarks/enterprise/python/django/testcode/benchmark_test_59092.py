# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59092(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
