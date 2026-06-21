# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
import ast


def BenchmarkTest20452(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    def _primary():
        return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
