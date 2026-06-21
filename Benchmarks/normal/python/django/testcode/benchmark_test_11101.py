# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast


def BenchmarkTest11101(request):
    xml_value = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    processed = data[:64]
    return JsonResponse({'error': str(processed), 'stack': repr(locals())}, status=500)
