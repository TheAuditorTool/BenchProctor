# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22752(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
