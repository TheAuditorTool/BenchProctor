# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00003(request):
    xml_value = request.body.decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    parsed = json.JSONDecoder().decode(str(data))
    return JsonResponse({'parsed': str(parsed)}, status=200)
