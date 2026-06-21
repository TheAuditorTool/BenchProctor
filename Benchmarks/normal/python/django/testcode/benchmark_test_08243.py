# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from app_runtime import db


def BenchmarkTest08243(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = comment_value if comment_value else 'default'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
