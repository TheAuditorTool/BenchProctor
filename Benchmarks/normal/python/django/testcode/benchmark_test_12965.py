# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest12965(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return JsonResponse({"saved": True})
