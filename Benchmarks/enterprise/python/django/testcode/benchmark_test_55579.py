# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from types import SimpleNamespace
from app_runtime import ssm_client


def BenchmarkTest55579(request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    ns = SimpleNamespace(payload=ssm_value)
    data = getattr(ns, 'payload')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
