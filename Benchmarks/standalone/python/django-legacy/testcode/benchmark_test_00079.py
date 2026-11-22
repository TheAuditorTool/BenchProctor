# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import re


def BenchmarkTest00079(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = str(forwarded_ip).replace('\x00', '')
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    find_user = etree.XPath('/users/user[@name="' + str(processed) + '"]')
    find_user(tree)
    return JsonResponse({"saved": True})
