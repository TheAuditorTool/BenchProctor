# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import requests


def BenchmarkTest68742(request):
    user_id = request.GET.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
