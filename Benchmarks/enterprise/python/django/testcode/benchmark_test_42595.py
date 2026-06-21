# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from app_runtime import auth_check


def BenchmarkTest42595(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ' '.join(str(origin_value).split())
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
