# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from app_runtime import auth_check


def BenchmarkTest10441(request):
    cookie_value = request.COOKIES.get('session_token', '')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(cookie_value), store_cred)
    return JsonResponse({"saved": True})
