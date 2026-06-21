# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import ast


def BenchmarkTest28920(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    return HttpResponse(str(data), content_type='text/html')
