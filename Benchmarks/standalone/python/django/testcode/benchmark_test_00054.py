# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import re
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00054(request):
    env_value = os.environ.get('APP_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.%~\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    etree.XPathEvaluator(tree)('/users/user[@name="' + str(processed) + '"]')
    return JsonResponse({"saved": True})
