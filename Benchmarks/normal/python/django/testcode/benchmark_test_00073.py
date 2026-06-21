# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest00073(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data, _sep, _rest = str(file_value).partition('\x00')
    auth_check('user', data)
    return JsonResponse({"saved": True})
