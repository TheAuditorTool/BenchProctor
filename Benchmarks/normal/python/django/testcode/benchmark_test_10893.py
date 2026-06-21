# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from dataclasses import dataclass
import json
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest10893(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = FormData(payload=json_value).payload
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
