# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from urllib.parse import unquote


def BenchmarkTest34347(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
