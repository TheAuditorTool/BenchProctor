# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00064(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = RequestPayload(comment_value).value
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    find_user = etree.XPath('/users/user[@name="' + str(processed) + '"]')
    find_user(tree)
    return JsonResponse({"saved": True})
