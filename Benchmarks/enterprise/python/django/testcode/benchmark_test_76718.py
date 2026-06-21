# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest76718(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    auth_check('user', ua_value)
    return JsonResponse({"saved": True})
