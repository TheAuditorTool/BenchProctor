# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from urllib.parse import unquote


def BenchmarkTest06703(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
