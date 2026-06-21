# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest08480(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
