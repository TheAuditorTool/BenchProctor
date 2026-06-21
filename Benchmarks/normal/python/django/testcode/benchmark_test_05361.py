# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from urllib.parse import unquote
from app_runtime import auth_check


def BenchmarkTest05361(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
