# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
from app_runtime import ssm_client


def BenchmarkTest09896(request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    def normalize(value):
        return value.strip()
    data = normalize(ssm_value)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
