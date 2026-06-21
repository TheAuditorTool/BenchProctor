# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest53058(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    auth_check('user', data)
    return JsonResponse({"saved": True})
