# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01287(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
