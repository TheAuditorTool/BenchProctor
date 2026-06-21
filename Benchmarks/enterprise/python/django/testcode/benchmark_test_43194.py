# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


request_state: dict[str, str] = {}

def BenchmarkTest43194(request):
    user_id = request.GET.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    _ev = {}
    eval(compile("_ev['r'] = HttpResponse(Template(data).render(Context()))", '<sink>', 'exec'))
    return _ev['r']
