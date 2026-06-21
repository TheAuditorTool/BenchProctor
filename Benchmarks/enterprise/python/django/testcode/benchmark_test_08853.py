# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import defusedxml.ElementTree


def BenchmarkTest08853(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value:.200s}'
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
