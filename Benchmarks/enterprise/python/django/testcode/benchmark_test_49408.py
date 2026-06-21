# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest49408(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    auth_check('user', data)
    return JsonResponse({"saved": True})
