# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


request_state: dict[str, str] = {}

def BenchmarkTest74075(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    def _primary():
        subprocess.Popen('echo ' + str(data), shell=True).wait()
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
