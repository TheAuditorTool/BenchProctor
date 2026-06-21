# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import ast


def BenchmarkTest76144(request):
    xml_value = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
