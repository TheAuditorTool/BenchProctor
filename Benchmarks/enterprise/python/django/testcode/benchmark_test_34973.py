# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import re


request_state: dict[str, str] = {}

def BenchmarkTest34973(request):
    raw_body = request.body.decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    return HttpResponse(Template(processed).render(Context()))
