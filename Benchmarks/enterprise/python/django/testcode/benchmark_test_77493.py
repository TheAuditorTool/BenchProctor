# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import json


def BenchmarkTest77493(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    Fernet(json_value.encode() if isinstance(json_value, str) else json_value).encrypt(b'data')
    return JsonResponse({"saved": True})
