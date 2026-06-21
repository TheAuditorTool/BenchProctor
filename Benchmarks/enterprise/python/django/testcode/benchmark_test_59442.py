# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
import ast


def BenchmarkTest59442(request):
    xml_value = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
