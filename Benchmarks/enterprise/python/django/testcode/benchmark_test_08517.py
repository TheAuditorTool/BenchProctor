# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest08517(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    if config_value:
        data = config_value
    else:
        data = ''
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
