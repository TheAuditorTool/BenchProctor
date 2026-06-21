# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import keyring
import ast
from app_runtime import ssm_client


def BenchmarkTest81459(request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    try:
        data = str(ast.literal_eval(ssm_value))
    except (ValueError, SyntaxError):
        data = ssm_value
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
