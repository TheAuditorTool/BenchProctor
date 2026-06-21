# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest04386(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = handle(ua_value)
    eval(compile('_parser = etree.XMLParser(resolve_entities=True, no_network=False)\netree.fromstring(str(data).encode(), _parser)', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
