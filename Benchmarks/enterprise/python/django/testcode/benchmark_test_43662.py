# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43662(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
