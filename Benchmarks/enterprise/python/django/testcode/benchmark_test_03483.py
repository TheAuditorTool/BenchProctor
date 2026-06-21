# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
from app_runtime import ssm_client


def BenchmarkTest03483(request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ssm_value)
    data = collected
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
