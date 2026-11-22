# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00110(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = RequestPayload(origin_value).value
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    etree.XPathEvaluator(tree)('/users/user[@name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
