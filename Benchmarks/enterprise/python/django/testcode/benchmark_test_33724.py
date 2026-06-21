# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from lxml import etree


def BenchmarkTest33724(request):
    env_value = os.environ.get('USER_INPUT', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(env_value).encode(), _parser)
    return JsonResponse({"saved": True})
