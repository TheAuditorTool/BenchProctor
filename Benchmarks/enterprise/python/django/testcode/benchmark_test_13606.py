# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13606(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
