# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
import ast


def BenchmarkTest71399(request):
    upload_name = request.FILES['upload'].name
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
