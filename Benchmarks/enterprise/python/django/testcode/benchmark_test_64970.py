# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import boto3


def BenchmarkTest64970(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    parts = []
    for token in str(file_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
