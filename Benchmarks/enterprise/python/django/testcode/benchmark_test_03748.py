# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest03748(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    reader = make_reader(auth_header)
    data = reader()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
