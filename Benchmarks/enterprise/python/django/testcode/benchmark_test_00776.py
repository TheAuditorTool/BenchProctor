# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest00776(request):
    user_id = request.GET.get('id', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(user_id).encode(), _parser)
    return JsonResponse({"saved": True})
