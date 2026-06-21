# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest49063(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    reader = make_reader(file_value)
    data = reader()
    auth_check('user', data)
    return JsonResponse({"saved": True})
