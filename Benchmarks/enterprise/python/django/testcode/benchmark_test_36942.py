# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest36942(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    auth_check('user', data)
    return JsonResponse({"saved": True})
