# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10485(request):
    raw_body = request.body.decode('utf-8')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
