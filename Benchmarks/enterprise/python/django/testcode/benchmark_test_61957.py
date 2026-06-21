# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def BenchmarkTest61957(request):
    xml_value = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
