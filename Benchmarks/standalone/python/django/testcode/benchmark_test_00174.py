# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import defusedxml.ElementTree


def BenchmarkTest00174(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = ' '.join(str(json_value).split())
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
