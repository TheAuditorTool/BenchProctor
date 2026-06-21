# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import json


def BenchmarkTest30431(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    try:
        data = json.loads(config_value).get('value', config_value)
    except (json.JSONDecodeError, AttributeError):
        data = config_value
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
