# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from types import SimpleNamespace


def BenchmarkTest16340(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    eval(compile('tree = etree.fromstring(b\'<users><user name="admin"/></users>\')\ntree.xpath(\'/users/user[name="\' + str(data) + \'"]\')', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
