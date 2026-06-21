# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest62154(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % str(xml_value)
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
