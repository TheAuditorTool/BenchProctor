# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest54176(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    if str(data).endswith(('.prod.internal', '.trusted.net')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
