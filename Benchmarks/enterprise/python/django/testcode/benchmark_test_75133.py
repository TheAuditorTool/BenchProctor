# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import defusedxml.ElementTree


def BenchmarkTest75133(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
