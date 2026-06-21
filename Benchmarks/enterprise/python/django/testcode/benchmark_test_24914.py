# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import shlex
import json


def BenchmarkTest24914(request):
    xml_value = request.body.decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
