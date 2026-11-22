# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00169(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    form = FormData(payload=auth_header)
    data = form.payload
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    find_user = etree.XPath('/users/user[@name="' + str(data) + '"]')
    find_user(tree)
    return JsonResponse({"saved": True})
