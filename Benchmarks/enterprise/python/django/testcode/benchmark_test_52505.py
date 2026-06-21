# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
import base64
from app_runtime import auth_check


def BenchmarkTest52505(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
