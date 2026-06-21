# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import json


def BenchmarkTest24554(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
