# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
from lxml import etree


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest51353(request):
    user_id = request.GET.get('id', '')
    data = default_blank(user_id)
    if time.time() > 1000000000:
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
