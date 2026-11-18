# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00424(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
