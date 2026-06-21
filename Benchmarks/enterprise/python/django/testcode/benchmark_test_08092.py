# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import boto3
import os


def relay_value(value):
    return value

def BenchmarkTest08092(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = relay_value(dotenv_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
