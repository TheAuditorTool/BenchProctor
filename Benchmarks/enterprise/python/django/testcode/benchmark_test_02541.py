# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from types import SimpleNamespace
from lxml import etree


def BenchmarkTest02541(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
