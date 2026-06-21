# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from dataclasses import dataclass
import json
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest59531(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
