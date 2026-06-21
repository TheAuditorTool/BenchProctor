# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest34195(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
