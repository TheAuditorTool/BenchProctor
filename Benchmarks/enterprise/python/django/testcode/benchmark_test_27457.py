# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest27457(request):
    cookie_value = request.COOKIES.get('session_token', '')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(cookie_value) + '"]')
    return JsonResponse({"saved": True})
