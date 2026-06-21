# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from urllib.parse import unquote
from app_runtime import auth_check


def BenchmarkTest30679(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
