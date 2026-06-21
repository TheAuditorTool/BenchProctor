# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import keyring
from app_runtime import db


def relay_value(value):
    return value

def BenchmarkTest03172(request):
    secret_value = 'default_config_label'
    data = relay_value(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return JsonResponse({"saved": True})
