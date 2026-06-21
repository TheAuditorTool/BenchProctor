# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from app_runtime import ssm_client


def BenchmarkTest32682(request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ssm_value)
    data = collected
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
