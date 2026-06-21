# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import json
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest12959(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
