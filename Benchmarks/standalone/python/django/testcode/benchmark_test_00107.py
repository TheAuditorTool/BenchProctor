# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest00107(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
