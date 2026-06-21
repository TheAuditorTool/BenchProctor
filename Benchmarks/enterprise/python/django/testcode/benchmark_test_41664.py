# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast


def BenchmarkTest41664(request):
    multipart_value = request.POST.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
