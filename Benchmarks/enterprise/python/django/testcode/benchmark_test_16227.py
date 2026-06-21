# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16227(request):
    xml_value = request.body.decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
