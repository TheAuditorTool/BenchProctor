# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from app_runtime import ssm_client


def BenchmarkTest47882(request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    data = ssm_value if ssm_value else 'default'
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
