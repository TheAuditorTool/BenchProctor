# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest00124(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = str(forwarded_ip).replace('\x00', '')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    etree.XPathEvaluator(tree)('/users/user[@name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
