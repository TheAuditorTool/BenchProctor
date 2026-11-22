# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00212(request, path_param):
    path_value = path_param
    form = FormData(payload=path_value)
    data = form.payload
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    etree.XPathEvaluator(tree)('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
