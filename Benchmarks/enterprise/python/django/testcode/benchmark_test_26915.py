# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest26915(request):
    xml_value = request.body.decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
