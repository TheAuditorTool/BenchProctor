# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import auth_check


def BenchmarkTest63230(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
