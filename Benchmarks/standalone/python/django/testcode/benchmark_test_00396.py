# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest00396(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
