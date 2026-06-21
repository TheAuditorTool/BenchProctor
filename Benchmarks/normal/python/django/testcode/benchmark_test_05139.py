# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest05139(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    auth_check('user', file_value)
    return JsonResponse({"saved": True})
