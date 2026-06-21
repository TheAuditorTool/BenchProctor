# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import pickle


def BenchmarkTest03225(request):
    user_id = request.GET.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    eval(compile("pickle.loads(data.encode('latin-1'))", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
