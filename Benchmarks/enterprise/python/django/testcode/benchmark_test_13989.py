# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest13989(request):
    raw_body = request.body.decode('utf-8')
    data = ensure_str(raw_body)
    auth_check('user', data)
    return JsonResponse({"saved": True})
