# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import json


def BenchmarkTest00023(request):
    upload_name = request.FILES['upload'].name
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
