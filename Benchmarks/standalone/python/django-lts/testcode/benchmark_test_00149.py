# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest00149(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        _coerced = float(ua_value)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    find_user = etree.XPath('/users/user[@name="' + str(processed) + '"]')
    find_user(tree)
    return JsonResponse({"saved": True})
