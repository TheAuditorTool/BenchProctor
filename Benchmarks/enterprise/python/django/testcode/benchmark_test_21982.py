# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import json


def BenchmarkTest21982(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = json.loads(file_value).get('value', '')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
