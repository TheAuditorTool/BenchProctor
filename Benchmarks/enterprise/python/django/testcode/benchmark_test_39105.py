# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39105(request):
    raw_body = request.body.decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
