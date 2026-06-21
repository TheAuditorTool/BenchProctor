# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
import json


def BenchmarkTest72157(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = '%s' % (json_value,)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
