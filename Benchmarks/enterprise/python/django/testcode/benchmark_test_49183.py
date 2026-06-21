# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def BenchmarkTest49183(request):
    xml_value = request.body.decode('utf-8')
    processed = shlex.quote(xml_value)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
