# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from app_runtime import auth_check


def BenchmarkTest78831(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(origin_value), store_cred)
    return JsonResponse({"saved": True})
