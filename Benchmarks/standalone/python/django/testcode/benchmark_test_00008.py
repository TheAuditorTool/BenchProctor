# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00008(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    reader = make_reader(ua_value)
    data = reader()
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    etree.XPathEvaluator(tree)('/users/user[@name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
