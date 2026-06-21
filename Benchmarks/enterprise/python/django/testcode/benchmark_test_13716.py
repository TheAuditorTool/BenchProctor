# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ast


def BenchmarkTest13716(request):
    user_id = request.GET.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    eval(compile("with open('/var/uploads/' + str(data), 'wb') as fh:\n    fh.write(b'data')", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
