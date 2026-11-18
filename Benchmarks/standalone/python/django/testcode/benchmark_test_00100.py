# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import re


def BenchmarkTest00100(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.%~\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
