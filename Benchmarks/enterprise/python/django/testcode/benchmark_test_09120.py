# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09120(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
