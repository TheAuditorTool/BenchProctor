# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from app_runtime import db


def BenchmarkTest56467(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(comment_value) + '"]')
    return JsonResponse({"saved": True})
