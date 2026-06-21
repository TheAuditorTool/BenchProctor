# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78269(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
