# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest67824(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    base_name = os.path.basename(str(json_value))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return JsonResponse({"saved": True})
