# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import boto3


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest03315(request):
    secret_value = 'default_config_label'
    reader = make_reader(secret_value)
    data = reader()
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
