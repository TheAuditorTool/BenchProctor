# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest15190(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    auth_check('user', data)
    return JsonResponse({"saved": True})
