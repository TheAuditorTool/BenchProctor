# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest71182(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
