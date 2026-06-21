# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest64643(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = default_blank(json_value)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return JsonResponse({"saved": True})
