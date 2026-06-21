# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


request_state: dict[str, str] = {}

def BenchmarkTest33858(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
