# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ast


def BenchmarkTest72427(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
