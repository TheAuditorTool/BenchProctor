# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest52197(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
