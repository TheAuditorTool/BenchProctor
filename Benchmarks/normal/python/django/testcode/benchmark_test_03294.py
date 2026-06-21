# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03294(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
