# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import base64


def BenchmarkTest52536(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
