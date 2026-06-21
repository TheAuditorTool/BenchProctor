# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


def BenchmarkTest03100(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
