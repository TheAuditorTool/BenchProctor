# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
from app_runtime import ssm_client


def BenchmarkTest05932(request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    if ssm_value:
        data = ssm_value
    else:
        data = ''
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
