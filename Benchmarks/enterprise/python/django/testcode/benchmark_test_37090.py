# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37090(request):
    raw_body = request.body.decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
