# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def relay_value(value):
    return value

def BenchmarkTest61162(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = relay_value(forwarded_ip)
    eval(compile('_parser = etree.XMLParser(resolve_entities=True, no_network=False)\netree.fromstring(str(data).encode(), _parser)', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
