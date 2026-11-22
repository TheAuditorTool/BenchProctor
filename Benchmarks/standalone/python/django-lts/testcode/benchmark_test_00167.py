# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00167(request, path_param):
    path_value = path_param
    form = FormData(payload=path_value)
    data = form.payload
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    etree.XPathEvaluator(tree)('/users/user[@name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
