# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import keyring


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest36258(request):
    secret_value = 'default_config_label'
    data = RequestPayload(secret_value).value
    store_cred = keyring.get_password('app', 'service-account')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
