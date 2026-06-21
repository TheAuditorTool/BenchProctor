# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from app_runtime import auth_check


def BenchmarkTest59759(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header:.200s}'
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
