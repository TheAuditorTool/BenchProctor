# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest75659(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value}'
    auth_check('user', data)
    return JsonResponse({"saved": True})
