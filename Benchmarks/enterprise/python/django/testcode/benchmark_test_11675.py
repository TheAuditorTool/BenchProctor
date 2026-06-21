# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest11675(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = '{}'.format(prop_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
