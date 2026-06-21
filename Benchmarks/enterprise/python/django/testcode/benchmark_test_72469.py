# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest72469(request):
    host_value = request.META.get('HTTP_HOST', '')
    reader = make_reader(host_value)
    data = reader()
    auth_check('user', data)
    return JsonResponse({"saved": True})
