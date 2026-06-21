# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import re


request_state: dict[str, str] = {}

def BenchmarkTest02807(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:_?&=\\-@]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return redirect(str(processed))
