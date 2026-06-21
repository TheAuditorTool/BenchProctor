# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46778(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
