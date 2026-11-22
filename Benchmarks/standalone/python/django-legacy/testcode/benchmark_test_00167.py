# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import re


def BenchmarkTest00167(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    if not re.fullmatch("^[a-zA-Z0-9 _.%~\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    find_user = etree.XPath('/users/user[@name="' + str(processed) + '"]')
    find_user(tree)
    return JsonResponse({"saved": True})
