# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest40772(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = json_value if json_value else 'default'
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
