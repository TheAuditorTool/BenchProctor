# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest02369(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = default_blank(file_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
