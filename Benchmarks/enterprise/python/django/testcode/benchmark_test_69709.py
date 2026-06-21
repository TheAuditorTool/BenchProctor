# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import boto3


def BenchmarkTest69709(request):
    secret_value = 'default_setting_value'
    data = '%s' % (secret_value,)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
