# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest00187(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = (lambda v: v.strip())(host_value)
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    etree.XPathEvaluator(tree)('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
