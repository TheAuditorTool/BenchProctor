# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from lxml import etree


def relay_value(value):
    return value

def BenchmarkTest12814(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = relay_value(multipart_value)
    if os.environ.get("APP_ENV", "production") != "test":
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
