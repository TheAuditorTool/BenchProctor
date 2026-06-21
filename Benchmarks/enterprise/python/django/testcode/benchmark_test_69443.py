# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from lxml import etree


def BenchmarkTest69443(request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
