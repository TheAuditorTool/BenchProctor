# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest04139(request, path_param):
    path_value = path_param
    data = default_blank(path_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
