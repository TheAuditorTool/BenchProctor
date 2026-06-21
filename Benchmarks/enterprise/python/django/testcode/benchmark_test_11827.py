# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
from types import SimpleNamespace


def BenchmarkTest11827(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    _ev = {}
    eval(compile('_ev[\'r\'] = HttpResponse(\'<script src="\' + str(data) + \'"></script>\', content_type=\'text/html\')', '<sink>', 'exec'))
    return _ev['r']
