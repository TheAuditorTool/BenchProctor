# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
from app_runtime import auth_check


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest69587(request):
    raw_body = request.body.decode('utf-8')
    data = RequestPayload(raw_body).value
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
