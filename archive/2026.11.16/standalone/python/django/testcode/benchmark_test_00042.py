# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest00042(request):
    host_value = request.META.get('HTTP_HOST', '')
    try:
        _coerced = float(host_value)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
