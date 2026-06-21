# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import defusedxml.ElementTree


def BenchmarkTest10849(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    defusedxml.ElementTree.fromstring(str(json_value))
    return JsonResponse({"saved": True})
