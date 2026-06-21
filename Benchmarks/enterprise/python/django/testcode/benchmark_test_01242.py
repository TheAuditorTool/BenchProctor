# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest01242(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    json.loads(data)
    return JsonResponse({"saved": True})
