# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest03156(request):
    host_value = request.META.get('HTTP_HOST', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
