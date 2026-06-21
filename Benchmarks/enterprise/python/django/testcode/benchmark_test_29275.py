# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest29275(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    os.chmod('/var/app/data/' + str(json_value), 0o777)
    return JsonResponse({"saved": True})
