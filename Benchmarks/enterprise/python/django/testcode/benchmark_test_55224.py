# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest55224(request):
    xml_value = request.body.decode('utf-8')
    data = normalise_input(xml_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
