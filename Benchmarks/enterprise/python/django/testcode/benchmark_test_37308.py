# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


request_state: dict[str, str] = {}

def BenchmarkTest37308(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
