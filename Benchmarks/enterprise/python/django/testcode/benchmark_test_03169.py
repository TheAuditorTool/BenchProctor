# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03169(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
