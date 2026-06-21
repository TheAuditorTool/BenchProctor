# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest27536(request):
    cookie_value = request.COOKIES.get('session_token', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(cookie_value).encode(), _parser)
    return JsonResponse({"saved": True})
