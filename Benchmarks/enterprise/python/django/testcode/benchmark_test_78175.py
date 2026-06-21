# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.shortcuts import redirect
import ast
import urllib.parse


def BenchmarkTest78175(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
