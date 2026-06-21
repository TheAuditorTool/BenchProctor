# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def coalesce_blank(value):
    return value or ''

def BenchmarkTest03757(request):
    xml_value = request.body.decode('utf-8')
    data = coalesce_blank(xml_value)
    def _primary():
        requests.get(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
