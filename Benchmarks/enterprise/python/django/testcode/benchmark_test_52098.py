# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest52098(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % str(host_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
