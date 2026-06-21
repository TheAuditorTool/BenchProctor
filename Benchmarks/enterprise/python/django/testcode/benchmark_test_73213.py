# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest73213(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    reader = make_reader(ua_value)
    data = reader()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
