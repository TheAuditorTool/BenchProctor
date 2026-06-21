# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest15298(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    auth_check('user', referer_value)
    return JsonResponse({"saved": True})
