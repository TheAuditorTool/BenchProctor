# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import auth_check


def BenchmarkTest23552(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
