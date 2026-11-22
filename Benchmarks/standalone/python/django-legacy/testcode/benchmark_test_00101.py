# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest00101(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    def normalize(value):
        return value.strip()
    data = normalize(forwarded_ip)
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    etree.XPathEvaluator(tree)('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
