# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time
import ast


def BenchmarkTest63354(request):
    multipart_value = request.POST.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
