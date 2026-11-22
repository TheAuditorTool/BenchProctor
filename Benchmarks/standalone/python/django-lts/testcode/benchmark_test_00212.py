# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import re


def BenchmarkTest00212(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    kind = 'json' if str(origin_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(origin_value).strip()
        case _:
            data = str(origin_value)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    etree.XPathEvaluator(tree)('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
