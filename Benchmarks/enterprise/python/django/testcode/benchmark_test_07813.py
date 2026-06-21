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

def BenchmarkTest07813(request):
    raw_body = request.body.decode('utf-8')
    data = handle(raw_body)
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return JsonResponse({"saved": True})
