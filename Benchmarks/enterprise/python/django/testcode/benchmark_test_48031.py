# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import boto3


def BenchmarkTest48031(request):
    secret_value = 'default_setting_value'
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(secret_value).encode())
    return JsonResponse({"saved": True})
