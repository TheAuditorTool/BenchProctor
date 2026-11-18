# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00626(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    reader = make_reader(ua_value)
    data = reader()
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
