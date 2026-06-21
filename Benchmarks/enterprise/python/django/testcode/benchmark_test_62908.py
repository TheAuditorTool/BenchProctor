# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import os


def BenchmarkTest62908(request):
    env_value = os.environ.get('USER_INPUT', '')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(env_value) + '"]')
    return JsonResponse({"saved": True})
