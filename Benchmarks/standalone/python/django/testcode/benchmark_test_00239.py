# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import re
import os


def BenchmarkTest00239(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = '%s' % str(env_value)
    if not re.fullmatch("^[a-zA-Z0-9 _.%~\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
