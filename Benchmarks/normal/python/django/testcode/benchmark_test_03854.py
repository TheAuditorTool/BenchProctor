# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


request_state: dict[str, str] = {}

def BenchmarkTest03854(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    _ev = {}
    eval(compile("link_path = os.path.join('/var/app/data', str(data))\ntarget = os.readlink(link_path)\nwith open(target, 'r') as fh:\n    content = fh.read()\n_ev['r'] = HttpResponse(content)", '<sink>', 'exec'))
    return _ev['r']
