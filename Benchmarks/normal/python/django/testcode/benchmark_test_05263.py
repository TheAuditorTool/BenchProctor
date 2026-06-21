# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest05263(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    auth_check('user', data)
    return JsonResponse({"saved": True})
