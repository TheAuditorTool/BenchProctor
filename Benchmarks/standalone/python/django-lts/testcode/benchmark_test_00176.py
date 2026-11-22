# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest00176(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    find_user = etree.XPath('/users/user[@name="' + str(data) + '"]')
    find_user(tree)
    return JsonResponse({"saved": True})
