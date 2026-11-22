# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00043(request):
    field_value = request.POST.get('field', '')
    form = FormData(payload=field_value)
    data = form.payload
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    find_user = etree.XPath('/users/user[@name="' + str(data) + '"]')
    find_user(tree)
    return JsonResponse({"saved": True})
