# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest54967(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    parts = str(file_value).split(',')
    data = ','.join(parts)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
