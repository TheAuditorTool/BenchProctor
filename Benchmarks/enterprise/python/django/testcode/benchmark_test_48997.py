# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import os


def BenchmarkTest48997(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
