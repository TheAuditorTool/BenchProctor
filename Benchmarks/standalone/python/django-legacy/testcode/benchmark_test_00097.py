# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00097(request):
    host_value = request.META.get('HTTP_HOST', '')
    reader = make_reader(host_value)
    data = reader()
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    find_user = etree.XPath('/users/user[@name="' + str(data) + '"]')
    find_user(tree)
    return JsonResponse({"saved": True})
