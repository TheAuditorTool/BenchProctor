# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import json


def BenchmarkTest57995(request):
    xml_value = request.body.decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
