# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


request_state: dict[str, str] = {}

def BenchmarkTest30940(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
