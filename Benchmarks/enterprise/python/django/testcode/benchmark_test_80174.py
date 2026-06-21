# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from urllib.parse import unquote


def BenchmarkTest80174(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
