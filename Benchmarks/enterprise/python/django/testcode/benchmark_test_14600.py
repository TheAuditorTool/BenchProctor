# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os


def BenchmarkTest14600(request):
    xml_value = request.body.decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
