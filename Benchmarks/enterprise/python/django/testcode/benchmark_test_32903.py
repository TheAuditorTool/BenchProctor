# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import ast
import urllib.parse


def BenchmarkTest32903(request):
    raw_body = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
