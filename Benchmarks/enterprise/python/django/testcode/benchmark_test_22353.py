# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import json
import os


def BenchmarkTest22353(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
