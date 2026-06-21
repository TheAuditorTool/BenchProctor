# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40433(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
