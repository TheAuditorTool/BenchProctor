# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import json
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest80988(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return JsonResponse({"saved": True})
