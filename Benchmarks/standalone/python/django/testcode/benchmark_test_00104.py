# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from app_runtime import db


def BenchmarkTest00104(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % (db_value,)
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
