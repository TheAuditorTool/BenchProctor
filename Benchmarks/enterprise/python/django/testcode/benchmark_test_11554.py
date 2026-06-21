# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest11554(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = '%s' % str(file_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
