# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
from lxml import etree


def normalise_input(value):
    return value.strip()

def BenchmarkTest70386(request):
    user_id = request.GET.get('id', '')
    data = normalise_input(user_id)
    if time.time() > 1000000000:
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
