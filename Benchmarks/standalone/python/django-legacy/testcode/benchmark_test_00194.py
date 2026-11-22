# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest00194(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ' '.join(str(ua_value).split())
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    find_user = etree.XPath('/users/user[@name="' + str(data) + '"]')
    find_user(tree)
    return JsonResponse({"saved": True})
