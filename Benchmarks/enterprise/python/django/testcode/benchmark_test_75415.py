# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ast


def BenchmarkTest75415(request):
    raw_body = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
