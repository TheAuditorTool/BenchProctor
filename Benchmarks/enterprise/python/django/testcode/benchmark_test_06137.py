# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import yaml
import ast
from app_runtime import ssm_client


def BenchmarkTest06137(request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    try:
        data = str(ast.literal_eval(ssm_value))
    except (ValueError, SyntaxError):
        data = ssm_value
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
