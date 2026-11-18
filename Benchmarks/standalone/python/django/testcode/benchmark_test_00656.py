# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from urllib.parse import unquote


def BenchmarkTest00656(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
