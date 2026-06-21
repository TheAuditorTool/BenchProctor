# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import re
import json


def coalesce_blank(value):
    return value or ''

def BenchmarkTest42145(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
