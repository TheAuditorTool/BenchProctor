# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import os
from types import SimpleNamespace


def BenchmarkTest14203(request):
    secret_value = 'default_setting_value'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
