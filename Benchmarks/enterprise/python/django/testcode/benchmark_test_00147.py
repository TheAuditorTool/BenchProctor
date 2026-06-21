# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00147(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
