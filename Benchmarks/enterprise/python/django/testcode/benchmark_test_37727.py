# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import yaml


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest37727(request):
    secret_value = 'feature_flag_value'
    data = RequestPayload(secret_value).value
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
