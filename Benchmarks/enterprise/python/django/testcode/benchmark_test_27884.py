# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest27884(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    os.remove(str(data))
    return JsonResponse({"saved": True})
