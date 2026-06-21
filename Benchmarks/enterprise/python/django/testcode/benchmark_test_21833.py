# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
import os


def BenchmarkTest21833(request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return JsonResponse({"saved": True})
