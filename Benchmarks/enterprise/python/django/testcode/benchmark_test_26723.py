# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import os
from types import SimpleNamespace


def BenchmarkTest26723(request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
