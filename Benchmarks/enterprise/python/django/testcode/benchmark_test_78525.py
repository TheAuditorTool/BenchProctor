# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78525(request):
    raw_body = request.body.decode('utf-8')
    prefix = ''
    data = prefix + str(raw_body)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
