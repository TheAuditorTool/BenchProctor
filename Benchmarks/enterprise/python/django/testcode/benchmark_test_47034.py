# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest47034(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    os.remove(str(data))
    return JsonResponse({"saved": True})
