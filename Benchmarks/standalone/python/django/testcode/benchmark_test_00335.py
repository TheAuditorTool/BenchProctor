# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from dataclasses import dataclass
import re


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00335(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    form = FormData(payload=header_value)
    data = form.payload
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
