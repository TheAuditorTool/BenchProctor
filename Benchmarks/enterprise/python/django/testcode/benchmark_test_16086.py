# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest16086(request):
    xml_value = request.body.decode('utf-8')
    os.system('echo ' + str(xml_value))
    return JsonResponse({"saved": True})
