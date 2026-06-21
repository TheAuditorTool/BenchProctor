# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest32386(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
