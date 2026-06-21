# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from app_runtime import auth_check


def coalesce_blank(value):
    return value or ''

def BenchmarkTest64039(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = coalesce_blank(ua_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
