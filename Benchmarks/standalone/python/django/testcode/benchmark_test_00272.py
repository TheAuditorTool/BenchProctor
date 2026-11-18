# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import re
from app_runtime import db


def BenchmarkTest00272(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
