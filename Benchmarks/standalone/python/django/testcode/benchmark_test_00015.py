# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest00015(request):
    user_id = request.GET.get('id', '')
    kind = 'json' if str(user_id).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(user_id).strip()
        case _:
            data = str(user_id)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
