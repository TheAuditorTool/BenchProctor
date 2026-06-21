# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import boto3
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest70204(request):
    secret_value = 'app_display_name'
    data = FormData(payload=secret_value).payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
