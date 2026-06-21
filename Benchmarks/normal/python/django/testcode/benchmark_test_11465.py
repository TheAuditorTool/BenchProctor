# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import keyring
import ast
from app_runtime import db


def BenchmarkTest11465(request):
    secret_value = 'feature_flag_value'
    try:
        data = str(ast.literal_eval(secret_value))
    except (ValueError, SyntaxError):
        data = secret_value
    store_cred = keyring.get_password('app', 'service-account')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return JsonResponse({"saved": True})
