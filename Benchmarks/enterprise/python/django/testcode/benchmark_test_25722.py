# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def normalise_input(value):
    return value.strip()

def BenchmarkTest25722(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = normalise_input(ua_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
