# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
import json


def BenchmarkTest04809(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
