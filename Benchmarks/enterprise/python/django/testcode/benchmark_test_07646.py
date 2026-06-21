# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest07646(request, path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    eval(compile("with open('/var/www/html/exports/report.txt', 'w') as fh:\n    fh.write(str(data))", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
