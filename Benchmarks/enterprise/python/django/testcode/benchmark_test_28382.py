# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest28382(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = f'{file_value:.200s}'
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
