# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest04949(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = default_blank(auth_header)
    _ev = {}
    eval(compile("link_path = os.path.join('/var/app/data', str(data))\ntarget = os.readlink(link_path)\nwith open(target, 'r') as fh:\n    content = fh.read()\n_ev['r'] = HttpResponse(content)", '<sink>', 'exec'))
    return _ev['r']
