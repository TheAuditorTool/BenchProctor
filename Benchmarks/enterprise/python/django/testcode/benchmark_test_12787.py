# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest12787(request, path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
