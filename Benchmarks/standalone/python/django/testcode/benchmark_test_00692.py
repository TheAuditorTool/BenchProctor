# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import re


def BenchmarkTest00692(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % (auth_header,)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
