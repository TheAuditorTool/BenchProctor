# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26624(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
