# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest00100(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '{}'.format(cookie_value)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    etree.XPathEvaluator(tree)('/users/user[@name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
