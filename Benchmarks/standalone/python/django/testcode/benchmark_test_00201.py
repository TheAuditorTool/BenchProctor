# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import re
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00201(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    if not re.fullmatch("^[a-zA-Z0-9 _.%~\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
