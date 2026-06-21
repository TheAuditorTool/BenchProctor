# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest08087(request):
    raw_body = request.body.decode('utf-8')
    data = default_blank(raw_body)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
