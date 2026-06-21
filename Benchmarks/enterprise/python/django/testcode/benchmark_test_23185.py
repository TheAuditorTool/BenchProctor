# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import ast
import urllib.parse


def BenchmarkTest23185(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
