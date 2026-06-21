# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest37197(request):
    user_id = request.GET.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return JsonResponse({'error': 'zero division'}, status=400)
    result = 100 / divisor
    return JsonResponse({"saved": True})
