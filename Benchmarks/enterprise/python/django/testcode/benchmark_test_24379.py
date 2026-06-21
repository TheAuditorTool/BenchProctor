# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest24379(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = coalesce_blank(ua_value)
    _ev = {}
    eval(compile("link_path = os.path.join('/var/app/data', str(data))\ntarget = os.readlink(link_path)\nwith open(target, 'r') as fh:\n    content = fh.read()\n_ev['r'] = HttpResponse(content)", '<sink>', 'exec'))
    return _ev['r']
