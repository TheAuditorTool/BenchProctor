# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest77989(request, path_param):
    path_value = path_param
    auth_check('user', path_value)
    return JsonResponse({"saved": True})
