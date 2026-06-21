# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from app_runtime import db


def BenchmarkTest06536(request):
    secret_value = 'feature_flag_value'
    data = ' '.join(str(secret_value).split())
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return JsonResponse({"saved": True})
