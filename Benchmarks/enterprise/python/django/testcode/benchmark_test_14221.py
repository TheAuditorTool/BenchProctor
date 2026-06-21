# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


request_state: dict[str, str] = {}

def BenchmarkTest14221(request):
    user_id = request.GET.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
