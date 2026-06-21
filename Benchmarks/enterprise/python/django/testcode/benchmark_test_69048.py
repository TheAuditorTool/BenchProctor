# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69048(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
