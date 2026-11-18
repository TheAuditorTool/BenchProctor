# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import json


def BenchmarkTest00710(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
