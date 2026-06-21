# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70294(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
