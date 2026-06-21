# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59596(request):
    xml_value = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
