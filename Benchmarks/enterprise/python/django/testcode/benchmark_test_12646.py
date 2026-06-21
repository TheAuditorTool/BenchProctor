# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest12646(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = handle(header_value)
    _ev = {}
    eval(compile('_ev[\'r\'] = HttpResponse(\'<script src="\' + str(data) + \'"></script>\', content_type=\'text/html\')', '<sink>', 'exec'))
    return _ev['r']
