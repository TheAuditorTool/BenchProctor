# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ast


def BenchmarkTest64341(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
