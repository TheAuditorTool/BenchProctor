# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import ast
from app_runtime import db


def BenchmarkTest07824(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    try:
        data = str(ast.literal_eval(profile_value))
    except (ValueError, SyntaxError):
        data = profile_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
