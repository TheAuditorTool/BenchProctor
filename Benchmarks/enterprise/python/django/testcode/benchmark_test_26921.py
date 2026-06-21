# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest26921(request):
    xml_value = request.body.decode('utf-8')
    data = default_blank(xml_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
