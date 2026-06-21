# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast


def BenchmarkTest61044(request):
    upload_name = request.FILES['upload'].name
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
