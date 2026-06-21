# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from app_runtime import ssm_client


def BenchmarkTest20038(request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    parts = str(ssm_value).split(',')
    data = ','.join(parts)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
