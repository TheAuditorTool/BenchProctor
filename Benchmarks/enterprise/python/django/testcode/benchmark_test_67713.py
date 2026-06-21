# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from app_runtime import auth_check


def BenchmarkTest67713(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = base64.b64decode(file_value).decode('utf-8', 'ignore')
    auth_check('user', data)
    return JsonResponse({"saved": True})
