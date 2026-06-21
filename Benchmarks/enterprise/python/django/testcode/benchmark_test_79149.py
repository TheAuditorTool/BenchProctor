# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import base64


def BenchmarkTest79149(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
