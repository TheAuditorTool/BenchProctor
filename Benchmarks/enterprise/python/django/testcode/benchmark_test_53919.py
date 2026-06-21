# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest53919(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
