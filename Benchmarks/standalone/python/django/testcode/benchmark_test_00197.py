# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest00197(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    os.system('echo ' + str(json_value))
    return JsonResponse({"saved": True})
