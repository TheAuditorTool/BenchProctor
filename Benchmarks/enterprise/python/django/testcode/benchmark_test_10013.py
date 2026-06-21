# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


request_state: dict[str, str] = {}

def BenchmarkTest10013(request):
    upload_name = request.FILES['upload'].name
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    def _primary():
        requests.get(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
