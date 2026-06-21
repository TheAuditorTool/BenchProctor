# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from lxml import etree


def normalise_input(value):
    return value.strip()

def BenchmarkTest07110(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = normalise_input(origin_value)
    if os.environ.get("APP_ENV", "production") != "test":
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
