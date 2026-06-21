# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest42418(request):
    upload_name = request.FILES['upload'].name
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
