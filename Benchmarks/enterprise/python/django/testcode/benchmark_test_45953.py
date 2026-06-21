# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import json
import os


def BenchmarkTest45953(request):
    host_value = request.META.get('HTTP_HOST', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    key = os.environ['DATA_ENC_KEY'].encode()
    with open('/var/log/app_audit.log', 'ab') as fh:
        fh.write(Fernet(key).encrypt(str(data).encode()))
    return JsonResponse({"saved": True})
