# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest51366(request, path_param):
    path_value = path_param
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(path_value) + '"]')
    return JsonResponse({"saved": True})
