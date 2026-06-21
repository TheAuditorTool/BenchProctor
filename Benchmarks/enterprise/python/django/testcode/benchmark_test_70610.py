# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import ast
import urllib.parse


def BenchmarkTest70610(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
